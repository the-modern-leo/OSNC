import unittest, os.path, time
from collections import namedtuple
import io
import xlsxwriter
from common import database
import Provision
from Provision.hardware import HardwareProvision
from Provision import hardware, gearrequest, settings, db

from Network import Network
from switchchecker import switchchecker
from openpyxl import load_workbook
from unittest.mock import patch, MagicMock, PropertyMock
from Provision.hardware import HardwareProvision
from datetime import date
import datetime
from Network.Network import Switch,Blade,Connection
from servicenow.servicenow import ServiceNow
from Tests.TestProvision.device_list.test_switches import future,past
from Provision import settings as hsettings
from servicenowreponses import newchangerequests



