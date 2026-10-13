import os
from datetime import datetime, timezone, timedelta
from unittest.mock import patch

import pytest

from business_object.stationstatus import StationStatus
from dao.station_status_dao import StationStatusDao
from dao.db_connection import DBConnection
from utils.reset_database import ResetDatabase


TZ = timezone(timedelta(hours=2))


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialize test data"""
    with patch.dict(os.environ, {"SCHEMA": "project_test_dao"}):
        ResetDatabase().run(test_dao=True)
        yield


def test_find_current_status_existing():
    """Find the latest status of an existing station."""

    # GIVEN
    dao = StationStatusDao()

    # WHEN
    status = dao.find_current_status(9901)

    # THEN
    assert status is not None
    assert isinstance(status, StationStatus)
    assert status.id_station == 9901
    assert status.horodatage == datetime(2026, 10, 13, 8, 30, tzinfo=TZ)
    assert status.nb_velos_dispos == 5
    assert status.nb_velos_elec_dispos == 2
    assert status.nb_places_dispos == 20


def test_find_current_status_non_existing():
    """Return None when a station has no status."""

    # GIVEN
    dao = StationStatusDao()

    # WHEN
    status = dao.find_current_status(9999)

    # THEN
    assert status is None


def test_find_current_status_latest_among_several():
    """Return the most recent status, not the oldest one."""

    # GIVEN
    dao = StationStatusDao()

    # WHEN
    status = dao.find_current_status(9902)

    # THEN
    assert status is not None
    assert status.nb_velos_dispos == 0
    assert status.nb_places_dispos == 16
    assert status.horodatage == datetime(2026, 10, 13, 8, 15, tzinfo=TZ)


def test_find_history():
    """Return the station history in chronological order."""

    # GIVEN
    dao = StationStatusDao()
    start_date = datetime(2026, 10, 13, 8, 0, tzinfo=TZ)
    end_date = datetime(2026, 10, 13, 8, 30, tzinfo=TZ)

    # WHEN
    history = dao.find_history(9901, start_date, end_date)

    # THEN
    assert isinstance(history, list)
    assert len(history) == 3
    assert all(isinstance(status, StationStatus) for status in history)
    assert [status.nb_velos_dispos for status in history] == [10, 8, 5]
    assert [status.horodatage for status in history] == [
        datetime(2026, 10, 13, 8, 0, tzinfo=TZ),
        datetime(2026, 10, 13, 8, 15, tzinfo=TZ),
        datetime(2026, 10, 13, 8, 30, tzinfo=TZ),
    ]


def test_find_history_empty():
    """Return an empty list when no status matches the period."""

    # GIVEN
    dao = StationStatusDao()
    start_date = datetime(2026, 10, 14, 8, 0, tzinfo=TZ)
    end_date = datetime(2026, 10, 14, 9, 0, tzinfo=TZ)

    # WHEN
    history = dao.find_history(9901, start_date, end_date)

    # THEN
    assert history == []


def test_create_status():
    """Successfully create a new station status."""

    # GIVEN
    dao = StationStatusDao()
    status = StationStatus(
        id_station=9910,
        horodatage=datetime(2026, 10, 13, 9, 0, tzinfo=TZ),
        nb_velos_dispos=7,
        nb_velos_elec_dispos=3,
        nb_places_dispos=12,
        est_installee=True,
        permet_retour=True,
        permet_emprunt=True,
    )

    # WHEN
    created = dao.create_status(status)

    # THEN
    assert created is True

    saved_status = dao.find_current_status(9910)
    assert saved_status is not None
    assert saved_status.nb_velos_dispos == 7
    assert saved_status.nb_velos_elec_dispos == 3
    assert saved_status.nb_places_dispos == 12