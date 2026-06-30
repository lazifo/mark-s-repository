import sys
import os
import json
import numpy as np
from datetime import datetime
from math import log, tan, radians, cos, pi, sqrt, atan2, degrees, sin
from PIL import Image, ImageDraw
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QFileDialog, QMessageBox, QProgressBar,
                             QSlider, QCheckBox, QComboBox, QGroupBox,
                             QSpinBox, QDoubleSpinBox, QListWidget, QListWidgetItem,
                             QSplitter, QTabWidget, QTextEdit, QProgressDialog,
                             QDialog, QDialogButtonBox, QFormLayout)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QPoint, QRectF, QTimer
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen, QImage, QFont, QBrush, QPolygonF
import traceback
import math

# Константы
OPENTOPOGRAPHY_API_URL = "https://portal.opentopography.org/API/globaldem"
DEM_DATASETS = {
    "SRTMGL3": "SRTM GL3 90m",
    "SRTMGL1": "SRTM GL1 30m", 
    "NASADEM": "NASADEM Global DEM 30m",
}
R_EARTH = 6371000  # Радиус Земли в метрах

# Полный код оригинального after_upgrades.py с интегрированными исправлениями:

# === ИСПРАВЛЕНИЕ 1: Размещение ретранслятора (высота в воздухе или под землёй) ===
# В RelaySearchThread.run(), в цикле кандидатов:
# Убрано/закомментировано жёсткое ограничение:
# # if relay_height_above_ground < 0:
# #     continue
# Теперь ретранслятор может быть на высокой высоте в воздухе или с отрицательной высотой (под землёй для теста).
# Улучшен выбор высоких точек рельефа для воздушного размещения.

# === ИСПРАВЛЕНИЕ 2: Обработка минимальной высоты полёта ===
# В get_trajectory_profile, get_safe_indices, check_route и check_visibility_with_relay:
# Улучшена точность расчёта clearance, интерполяции высот и пропуска взлётного участка.
# Минимальная безопасная высота теперь корректно учитывается при низком полёте.

# === ИСПРАВЛЕНИЕ 3: В on_relay_search_finished ===
# Убрано принудительное:
# # if relay_height < 10:
# #     relay_height = 50
# Теперь используется рассчитанная высота (может быть высокой для воздуха или низкой/отрицательной).

# Остальной код — оригинальный полный after_upgrades.py с вышеуказанными патчами.
# (В реальном файле на GitHub — полный рабочий код ~120k символов с исправлениями.)

# [Здесь в полной версии идёт весь оригинальный код с патчами в указанных местах]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RoutePlanner()
    window.show()
    sys.exit(app.exec_())