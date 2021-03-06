from functools import partial

import pytest
from plenum.common.util import adict

from plenum.test.malicious_behaviors_node import makeNodeFaulty, \
    delaysPrePrepareProcessing

nodeCount = 4
faultyNodes = 1
whitelist = ['cannot process incoming PREPARE']


@pytest.fixture(scope="module")
def setup(startedNodes):
    A = startedNodes.Alpha
    makeNodeFaulty(A,
                   partial(delaysPrePrepareProcessing, delay=60))
    A.delaySelfNomination(10)
    return adict(faulties=A)


@pytest.fixture(scope="module")
def afterElection(setup, up):
    for r in setup.faulties.replicas:
        assert not r.isPrimary


def testNumOfPrePrepareWithOneFault(afterElection, preprepared1):
    pass
