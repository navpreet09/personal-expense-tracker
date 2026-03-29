# Strategy pattern: defines different behaviors for generating summaries
class SummaryStrategy:
    def generate_summary(self, expenses):
        pass

class MonthlySummaryStrategy(SummaryStrategy):

    def generate_summary(self, expenses):
        total = 0
        for expense in expenses:
            total += expense.amount

        return f"Monthly total spending: {total}"
    
class TotalSummaryStrategy(SummaryStrategy):
    def generate_summary(self, expenses):
        total = 0
        for expense in expenses:
            total += expense.amount

        return f"Total spending: {total}"

