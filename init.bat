@echo off
setlocal

cd /d %~dp0

echo #............................................................#
echo #                                                            #
echo #                                                            #
echo #    Download_Links_from Website Init                        # 
echo #                                                            #
echo #                                                            #
echo #............................................................#
echo.


if not exist ".venv\Scripts\activate.bat" (
	echo.
	echo The virtal enviroment does not exist. 
	echo Will try to make the enviroment.
	echo.
	
	python -m venv .venv
)

call .venv\Scripts\activate.bat
if exist requirements.txt (
	python -m pip install -r requirements.txt
)
:: python -m pip install --upgrade --force-reinstall -r requirements.txt
call .venv\Scripts\deactivate.bat

echo.
echo Done .....
echo.
