from src.models.kitaev_chain import KitaevChain

def test_hamiltoniano_size():
    kc = KitaevChain(N=5)
    H = kc.hamiltoniano()
    assert H.shape == (5,5)
