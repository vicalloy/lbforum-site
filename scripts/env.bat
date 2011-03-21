@echo off
@call %~dp0..\env\Scripts\activate.bat
@set mg=python.exe %~dp0..\lbforum_site\manage.py
@cmd
