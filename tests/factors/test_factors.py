# -*- coding: utf-8 -*-
from zvt.factors.z.z_factor import ZFactor


def test_z_factor():
    z = ZFactor(
        codes=["000338"],
        need_persist=False,
        provider="joinquant",
    )
    z.draw(show=True)

    z = ZFactor(
        codes=["000338", "601318"],
        need_persist=True,
        provider="joinquant",
    )
    z.draw(show=True)
