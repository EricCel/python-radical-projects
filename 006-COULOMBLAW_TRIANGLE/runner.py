import decimal as dl
import typing as tp

k : tp.Final = dl.Decimal('9E9')

class Charge(tp.NamedTuple) :
    charge : dl.Decimal
    mts : dl.Decimal|None = None

q2 : Charge = Charge(dl.Decimal('6E-10'))
q1 : Charge = Charge(dl.Decimal('6E-9'), dl.Decimal('3E-2'))
q3 : Charge = Charge(dl.Decimal('3E-8'), dl.Decimal('5E-2'))

def coulomb_trigonometry(main:Charge, first:Charge, second:Charge) -> dl.Decimal:
    charges : list[Charge] = [first, second]
    forces : list[dl.Decimal] = []
    for c in charges :
        force : dl.Decimal = (k * c.charge * main.charge) / c.mts ** dl.Decimal(2) # type:ignore
        forces.append(force) # type:ignore

    real_force : dl.Decimal = forces[0] ** dl.Decimal('2') + forces[1] ** dl.Decimal('2')
    real_force : dl.Decimal = real_force.sqrt()

    print(f'{real_force}N')         
    return real_force

coulomb_trigonometry(q2, q1, q3)