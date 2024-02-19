from typing import Any

from models.damage_loss import DamageLoss
from models.damage_loss_detail import DamageLossDetail
from models.search_filter import SearchFilter
from database.queries import *
from database.db_template import VoucherTemplate


class DamageLossDatabase(VoucherTemplate):

    # add, modify ,delete

    def add(self, damage_loss: DamageLoss,
            damage_loss_details: list[DamageLossDetail]):
        queries = (damage_loss_add, damage_loss_detail_add)
        params = damage_loss.to_tuple_db_without_id()
        return super().add_detail("Damage Loss", queries, params, damage_loss_details)

    def modify(self, damage_loss: DamageLoss,
               damage_loss_details: list[DamageLossDetail],
               delete_ids: list[Any]):
        queries = (damage_loss_modify, damage_loss_detail_modify,
                   damage_loss_detail_delete)
        params = damage_loss.to_tuple_db()
        target_id = damage_loss.damage_loss_id
        return super().modify_detail("Damage Loss", queries, params, damage_loss_details, delete_ids, target_id)

    def delete(self, damage_loss_id: int):
        query = damage_loss_delete
        return super().delete_detail("Damage Loss", query, damage_loss_id)

    # Views

    def view(self, search_filter: SearchFilter):
        queries = (damage_loss_view_base, damage_loss_view_where_trandate)
        return super().view_voucher(search_filter, queries)

    def view_details(self, damage_loss_id: int):
        query = damage_loss_detail_view_by_damage_loss_id
        return super().view_voucher_details(query, damage_loss_id)
