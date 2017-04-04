"""

Testing ground for parallel backend

"""
import gc

from mlens.utils.dummy import LayerGenerator, Data, Cache
from mlens.parallel.tests.funcs import (layer_fit, layer_predict,
                                        layer_transform,
                                        lc_fit, lc_from_file, lc_predict,
                                        lc_transform)

LEN = 6
WIDTH = 2
FOLDS = 3
MOD, r = divmod(LEN, FOLDS)
assert r == 0

lg = LayerGenerator()
data = Data('blend', True, True)

X, y = data.get_data((LEN, WIDTH), MOD)
(F, wf), (P, wp) = data.ground_truth(X, y, 1, False)

layer = lg.get_layer('blend', True, True)
lc = lg.get_layer_container('blend', True, True)

layer.indexer.fit(X)

cache = Cache(X, y, data)

def test_layer_fit():
    """[Parallel | Stack | Prep | Proba] test layer fit."""
    layer_fit(layer, cache, F, wf)

def test_layer_predict():
    """[Parallel | Stack | Prep | Proba] test layer fit."""
    layer_predict(layer, cache, P, wp)

def test_layer_transform():
    """[Parallel | Stack | Prep | Proba] test layer fit."""
    layer_transform(layer, cache, F)

def test_lc_fit():
    """[Parallel | Stack | Prep | Proba] test layer container fit."""
    lc_fit(lc, X, y, F, wf)

def test_lc_predict():
    """[Parallel | Stack | Prep | Proba] test layer container predict."""
    lc_predict(lc, X, P, wp)

def test_lc_transform():
    """[Parallel | Stack | Prep | Proba] test layer container transform."""
    lc_transform(lc, X, F)

def test_lc_file():
    """[Parallel | Stack | Prep | Proba] test layer container from file."""
    lc_from_file(lc, cache, X, y, F, wf, P, wp)

def test_close():
    """[Parallel | Stack | Prep | Proba] close cache."""
    cache.terminate()
