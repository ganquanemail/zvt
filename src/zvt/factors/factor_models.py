# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Dict, Union, List, Optional

from pydantic import BaseModel, field_validator, Field
from pydantic_core.core_schema import ValidationInfo

from zvt.contract import IntervalLevel, AdjustType
from zvt.contract.model import MixinModel
from zvt.tag.common import StockPoolType
from zvt.tag.tag_utils import get_main_tags, get_sub_tags, get_hidden_tags, get_stock_pool_names
from zvt.trader import TradingSignalType
from zvt.utils import date_time_by_interval, current_date


class FactorRequestModel(BaseModel):
    factor_name: str
    entity_ids: Optional[List[str]]
    data_provider: str = Field(default="em")
    start_timestamp: datetime = Field(default=date_time_by_interval(current_date(), -365))
    level: IntervalLevel = Field(default=IntervalLevel.LEVEL_1DAY)


class KdataRequestModel(BaseModel):
    entity_ids: List[str]
    data_provider: str = Field(default="em")
    start_timestamp: datetime = Field(default=date_time_by_interval(current_date(), -365))
    end_timestamp: Optional[datetime] = Field(default=None)
    level: IntervalLevel = Field(default=IntervalLevel.LEVEL_1DAY)
    adjust_type: AdjustType = Field(default=AdjustType.hfq)


class KdataModel(BaseModel):
    entity_id: str
    code: str
    name: str
    level: IntervalLevel = Field(default=IntervalLevel.LEVEL_1DAY)
    datas: List


class TradingSignalModel(BaseModel):
    entity_id: str
    happen_timestamp: datetime
    due_timestamp: datetime
    trading_level: IntervalLevel = Field(default=IntervalLevel.LEVEL_1DAY)
    trading_signal_type: TradingSignalType
    position_pct: Optional[float] = Field(default=0.2)
    order_amount: Optional[float] = Field(default=None)
    order_money: Optional[float] = Field(default=None)


class FactorResultModel(BaseModel):
    entity_ids: Optional[List[str]]
    tag_reason: str
