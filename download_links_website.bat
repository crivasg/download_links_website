@echo off
setlocal

cd /d %~dp0

echo #............................................................#
echo #                                                            #
echo #                                                            #
echo #    download_links_website                                  # 
echo #                                                            #
echo #                                                            #
echo #............................................................#
echo.


if not exist ".venv\Scripts\activate.bat" (
	call %~dp0\init.bat 
)

CALL .venv\Scripts\activate.bat
IF -%1- == -- (
	python -m download_links_website --help
	CALL .venv\Scripts\deactivate.bat
	EXIT /b 1
)

IF -%2- == -- (
	python -m download_links_website --input "%1"
) ELSE (
	python -m download_links_website --input "%1" --dest_folder "%2"
)
CALL .venv\Scripts\deactivate.bat

ECHO.

EXIT /b 0

:: https://www.dynaexamples.com/implicit/yaris-static-suspension-system-loading/zip-for-download.zip
:: https://www.dynaexamples.com/dynaexamples/thermal/welding-new/welding-solids/exp_welding_solids-tar.gz
:: https://www.steel.org/steel-markets/automotive/gdis/presentations/?_kw=^&_author=^&_submitter=^&_category=^&_title=^&_year=2023^&_track=^&_session=^&_organization=
:: https://www.beta-cae.com/resources.htm


:: References:
:: - https://stackoverflow.com/a/6135689
