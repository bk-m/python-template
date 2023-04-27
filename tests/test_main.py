import logging
from typing import Self

import pytest
from _pytest.logging import caplog

from app.main import main


class TestMain:
    def test_output(self: Self, caplog: caplog) -> None:
        caplog.set_level(logging.DEBUG)
        main()
        records = caplog.get_records("call")
        assert len(records) == 1
        assert "Hello, World!" in records[0].message

    @pytest.mark.xfail()
    def test_expected_to_fail(self: Self, caplog: caplog) -> None:
        caplog.set_level(logging.DEBUG)
        main()
        records = caplog.get_records("call")
        assert len(records) == 1
