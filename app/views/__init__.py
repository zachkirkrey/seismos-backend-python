# flake8: noqa F401
from .auth import Login
from .project import Project, ProjectCreate
from .tracking_sheet import TrackingSheet, CreateTrackingSheet
from .oc_report import OCReport, OCReportExport
from .input_data import InputData
from .daily_log import DailyLog
from .deafult_value import DefaultValue

ENDPOINTS_MAP = {
    Login: "/auth",
    Project: "/project/<project_id>",
    ProjectCreate: "/project",
    TrackingSheet: "/tracking-sheet/<tracking_sheet_id>",
    CreateTrackingSheet: "/tracking-sheet",
    OCReport: "/oc-report",
    OCReportExport: "/oc-report/export",
    InputData: "/input-data",
    DailyLog: "/daily-log",
    DefaultValue: "/default-value",
}
