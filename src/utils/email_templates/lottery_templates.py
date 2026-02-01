class LotteryEmailTemplate:
    @staticmethod
    def lottery_win_template_1(lottery_event, ballot):
        email_body = (
            f"Congrats! you have won a lottery! Details are shared bellow:\n"
            f"Lottery Event Title: {lottery_event.title}\n"
            f"Ballot Number: {ballot.ballot_number}\n"
            f"Prize Money: {lottery_event.prize_money}"
        )
        return email_body
