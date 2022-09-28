@echo off
setlocal
cd %~dp0
call .\venv\Scripts\activate
python -m QantasWineBonusPointsLister
