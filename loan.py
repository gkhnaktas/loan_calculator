loan = 1_000_000        # loan amount
interest = 0.025        # monthly interest
taxes = 0.15 + 0.15     # total taxes
number = 12             # loan term (months)

interest_total = interest * (1 + taxes)

payment = (interest_total * loan) / (1 - (1 + interest_total)**(-1 * number))

print("-" * 78)
print(f"{'#':<3}  {'payment':<13}  {'payback':<13}  {'interest':<13}  {'taxes':<13}  {'left':<15}")
print("-" * 78)

payback_t = 0
interest_t = 0
taxes_t = 0

for _ in range(1, number + 1):
    if _ == 1:
        left = loan
    i = left * interest_total
    _i = left * interest
    _taxes = _i * taxes
    payback = payment - i
    left = abs(left - payback)
    print(f"{_:<3}  {payment:<13,.2f}  {payback:<13,.2f}  {_i:<13,.2f}  {_taxes:<13,.2f}  {left:<15,.2f}")

    payback_t += payback
    interest_t += _i
    taxes_t += _taxes

print("-" * 78)
print(f"{'#':<3}  {payment * number:<13,.2f}  {payback_t:<13,.2f}  {interest_t:<13,.2f}  {taxes_t:<13,.2f}")
print("-" * 78)
