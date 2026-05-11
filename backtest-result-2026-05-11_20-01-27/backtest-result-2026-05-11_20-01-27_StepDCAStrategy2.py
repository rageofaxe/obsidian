from freqtrade.strategy import IStrategy
from pandas import DataFrame
import talib.abstract as ta
from freqtrade.persistence import Trade
import logging

logger = logging.getLogger(__name__)
logger.info(f"INIT")
class StepDCAStrategy2(IStrategy):
    # Общий профит +5% для закрытия всей позиции
    # 5m
    # minimal_roi = {"0": 0.020}
    # 1h
    minimal_roi = {"0": 0.03}
    # Финальный стоп-лосс на случай падения после последнего добора
    stoploss = -0.99
    timeframe = '1h'

    # Включаем усреднение (DCA)
    position_adjustment_enable = True
    # Позволяет суммарно вложить до 100% (10+20+30+40)
    max_entry_multiplier = 10 

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Индикаторы для условий входа (например, RSI)
        logger.info(f"populate")
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod=14)
        stoch = ta.STOCH(dataframe)
        dataframe['slowk'] = stoch['slowk']
        dataframe['slowd'] = stoch['slowd']
        return dataframe

    def populate_entry_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        # Условие для открытия САМОГО ПЕРВОГО ордера
        logger.info(f"OPENORDER")
        dataframe.loc[
            (dataframe['rsi'] < 35) &
            (dataframe['slowk'] > 20) &
            (dataframe['slowk'] < 40) & 
            (dataframe['slowk'] < dataframe['slowd']) 
        , 'enter_long'] = 1
        return dataframe

    def populate_exit_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        return dataframe

    def custom_stake_amount(self, pair: str, current_time: str, current_rate: float,
                            proposed_stake: float, min_stake: float, max_stake: float,
                            entry_tag: str, side: str, **kwargs) -> float:
        # Шаг 1: Первый вход на 10% от депозита
        return self.wallets.get_total_stake_amount() * 0.05

    def adjust_trade_position(self, trade: Trade, current_time: str,
                              current_rate: float, current_profit: float,
                              min_stake: float, max_stake: float,
                              **kwargs):
        
        # Считаем количество уже исполненных ордеров в этой сделке
        count_of_entries = trade.nr_of_successful_entries
        total_balance = self.wallets.get_total_stake_amount()

        # Шаг 2: Если цена упала на 5% от первого входа (1 ордер уже есть)
        if count_of_entries == 1 and current_profit <= -0.05:
            logger.info(f"First adjust {current_profit}")
            return total_balance * 0.1

        # Шаг 3: Если упала на 10% (уже 2 ордера в позиции)
        if count_of_entries == 2 and current_profit <= -0.1: # Профит считается от средней цены
            logger.info(f"Second adjust {current_profit}")
            return total_balance * 0.15

        # Шаг 4: Третий добор на 40%, если цена упала еще ниже (уже 3 ордера)
        if count_of_entries == 3 and current_profit <= -0.2:
            logger.info(f"Third adjust {current_profit}")
            return total_balance * 0.20
        
        # Шаг 5: Четвертый добор на 40%, если цена упала еще ниже (уже 3 ордера)
        if count_of_entries == 4 and current_profit <= -0.4:
            logger.info(f"Fourth adjust {current_profit}")
            return total_balance * 0.20
        
        # Шаг 5: Четвертый добор на 40%, если цена упала еще ниже (уже 3 ордера)
        if count_of_entries == 5 and current_profit <= -0.6:
            logger.info(f"Fifth adjust {current_profit}")
            return total_balance * 0.30
        
        if count_of_entries == 5:
            logger.info(f"LOSE?")
    
        return None
