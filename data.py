def __check_status(
    self,
    bnpl_last_usable_target_status: Status,
    customer_credit_last_usable_target_status: Status,
) -> (bool, Status):
    anonymous_data_status = self.__status_repository.get("anonymous_data")

    if (
        anonymous_data_status.is_update()
        and anonymous_data_status.get_date() < bnpl_last_usable_target_status.get_date()
        and anonymous_data_status.get_date()
        < customer_credit_last_usable_target_status.get_date()
    ):
        logger.info("Update with minimum of source dates")
        min_date = min(
            bnpl_last_usable_target_status.get_date(),
            customer_credit_last_usable_target_status.get_date(),
        )
        anonymous_data_status.set_date(min_date)
        anonymous_data_status.set_updating()
        return True, anonymous_data_status
    else:
        logger.info("Updated!")
        return False, anonymous_data_status
