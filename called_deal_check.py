
import requests
import json
import csv
import os
from dotenv import load_dotenv

deal_list_file_path = r"I:\python_projects\Called Deal Check\deal_list.csv"
deal_output_path = r"I:\python_projects\Called Deal Check\deal_output.csv"
json_dump_file = r"I:\python_projects\Called Deal Check\json_deal_dump.csv"

load_dotenv()
api_key = os.environ.get("ACCESS_KEYCODE")

all_data = []
deal_list = ['FHMT0603','WMS04S01','WFM08AR2','TMT0513S','SURF06B4','SAS05010','SAS05AR1','RFC07QH9','CHT06NC1','SAR043AC']

#with open(deal_list_file_path, "r") as csv_file:
#    reader = csv.DictReader(csv_file, fieldnames=["dealname"])
#    for row in reader:
#        deal_list.append(row["dealname"])

# Connectivity test. We should be able to hit the APSEC intex server and get the library version number
resp = requests.get('http://api.apsec.com/rest/intex/v2/version')
print('Response Code: {}'.format(resp.status_code))
print('Response Text: {}'.format(resp.text))

for deal in deal_list:

    deal_name = deal
    settle_date = "20180528"
    settle_date_prior = "20180428"

    task = [{
        "function": "DEAL_INFO",
        "params": {
            "INIT": {
                "DEFAULT": {
                    "KEYVAL_DELIM_ASCII": "10"
                },
                "CASE_SENITIVE": {

                }
            },
            "DEAL_HANDLE": {
                "DEFAULT": {
                    "ADDITIONAL_REQUIRED_ASSET_INFOS": "INTEXCALC_REIN_OVR_ID|",
                    "ADDL_MBSPOOL_FILES": "GEO",
                    "ADDL_MBSPOOL_INFO_FOR_REMICS": "0",
                    "ALLOW_ACCESS_KNOWN_CF_NMON": "FROM_SCHEDULED_PAYDATE",
                    "ALLOW_REREMIC_CHILD_CF_ACCESS": "REFERRED_CHILD_DEAL_ONLY",
                    "CDU_LOOKBACK_LIMIT_MODE": "NONE",
                    "COLLAT_LIST_TOP_LEVEL": "1",
                    "CUSIP_TABLES": "CMO|ISIN|CSI|DUS|MGP|MBS|BBGTK|BBGDEAL|BBGID|BDC",
                    "DECIMAL_DIGITS_CF_GAP": "2",
                    "DECIMAL_DIGITS_CF_TABLE": "9",
                    "DECIMAL_DIGITS_CONVEX": "9",
                    "DECIMAL_DIGITS_COUP_FAC": "9",
                    "DECIMAL_DIGITS_CP": "9",
                    "DECIMAL_DIGITS_DEC_TABLE": "0",
                    "DECIMAL_DIGITS_DISCOUNTMARGIN": "9",
                    "DECIMAL_DIGITS_DURN": "9",
                    "DECIMAL_DIGITS_FACTOR": "9",
                    "DECIMAL_DIGITS_PERCENT": "9",
                    "DECIMAL_DIGITS_PRICE": "9",
                    "DECIMAL_DIGITS_SPREAD": "9",
                    "DECIMAL_DIGITS_SYMVAR_TABLE": "9",
                    "DECIMAL_DIGITS_TICS": "0",
                    "DECIMAL_DIGITS_TRIGGER_VAL": "9",
                    "DECIMAL_DIGITS_WAL": "9",
                    "DECIMAL_DIGITS_WAVG_INTEGER": "9",
                    "DECIMAL_DIGITS_YIELD": "9",
                    "DO_EXPLODE_MEGAS": "0",
                    "DO_FORMAT_TRIGVALS": "1",
                    "EXCLUDE_PREFUND_FROM_TERMS": "1",
                    "EXTENSIVE_ERROR_CHECKING": "FATAL",
                    "FORMAT_DURATION_AS_INTEGER": "1",
                    "FULL_CASHFLOW_DETAIL": "FULL",
                    "GET_ABS_SUMMARY_FROM_LATEST_CDU": "1",
                    "GET_CHILD_TRIGGERS": "1",
                    "HIDE_MODELING_TRANCHES": "0",
                    "HIDE_RESTRICTED_TRANCHES": "1",
                    "IGNORE_DESCRIPTIVE_INFO": "NONE",
                    "IGNORE_PAIDDOWN_COLLAT": "1",
                    "INCLUDE_PNOTES": "1",
                    "INCLUDE_UNDEFINED_ASSET_INFOS": "1",
                    "LOANS_CONTROLS_LIMIT": "0",
                    "MAKE_XRS_TRANCHE": "1",
                    "MAX_SCHED_ELEMENTS": "ALL",
                    "MAX_THREADS": "8",
                    "N_PREDEFINED_VARS": "3",
                    "PNOTE_MAIN_AS_COLLAT": "0",
                    "PREDEFINED_VAR[1]": "#_IGNORE_INFO_ONLY_CDU_AS_LATEST_CDU",
                    "PREDEFINED_VAR[2]": "#EDWCOLLAT_FORCE_USE_CLUSTER_SECTION",
                    "PREDEFINED_VAR[3]": "#_LANG_FORCE_ENGLISH",
                    "PRICE_TICS_DECIMAL": "DECIMAL",
                    "REPORT_INDEX_LISTS_TO_RUN_WITH_PROXY": "1",
                    "REQUIRE_CLEANUP_PRECISION": "0",
                    "SHOW_GROUP_NAMES": "1",
                    "SHOW_HEDGE_TRANCHES": "HEDGENET",
                    "SHOW_INTERNAL_DATA_ITEMS": "1",
                    "SHOW_PSEUDO_TRANCHES": "1",
                    "SINGLE_TRANCHE_MODE": "1",
                    "STRUCTURED_ASSET_DATA_PREFERRED_SOURCE": "INTEX_DETERMINED",
                    "TAG_TRANCHE_WITH_PROVIDED_IDENTIFIER": "1",
                    "TRADING_ACCURACY_NOT_REQUIRED": "1",
                    "USE_DUEBILL": "ZERO_DELAY_BONDS",
                    "USE_HIST_ALL": "ASOFDATE_BASE_ONLY",
                    "USE_VINDEX0": "0",
                    "VALID_DATES_ONLY": "1",
                    "YLDCRV_NODES": "COMMON|1YR|3YR|7YR"
                },
                "CASE_SENITIVE": {
                    "ACCESS_CLIENT": "AMHERST INSIGHTLABS, LLC - AMHERST PIERPONT SECURITIES",
                    "ACCESS_KEYCODE": api_key,
                    "CDI_PATH": "/mnt/intexshare/intex/cmo_cdi",
                    "CDU_PATH": "/mnt/intexshare/intex/cmo_cdu"
                }
            },
            "DEAL_OPTIONS": {
                "DEFAULT": {
                    "DEAL_NAME": deal_name,
                    "DEAL_MODE": "SEASONED_POOLS",
                    "DO_OPTIMIZE_CLUSTERING": "0",
                    "DO_STRAT_COLLAT": "0",
                    "FACE_AMOUNT_SCALE_BASIS": "SUGGESTED_BAL",
                    "PARSE_CONTROL": "TYPICAL",
                    "SETTLE_YYYYMMDD": settle_date
                },
                "CASE_SENITIVE": {

                }
            },
            "DEAL_INFO": {
                "DEFAULT": {
                    "DEAL_INFO_DEALNAME": deal_name,
                    "DEAL_INFO_TRANCHENAME": "COLLAT",  # defaults all info to deal level stats
                    "DECIMAL_DIGITS_CF_GAP": "2",
                    "DECIMAL_DIGITS_CF_TABLE": "9",
                    "DECIMAL_DIGITS_CONVEX": "9",
                    "DECIMAL_DIGITS_COUP_FAC": "9",
                    "DECIMAL_DIGITS_CP": "9",
                    "DECIMAL_DIGITS_DEC_TABLE": "0",
                    "DECIMAL_DIGITS_DISCOUNTMARGIN": "9",
                    "DECIMAL_DIGITS_DURN": "9",
                    "DECIMAL_DIGITS_FACTOR": "9",
                    "DECIMAL_DIGITS_PERCENT": "9",
                    "DECIMAL_DIGITS_PRICE": "9",
                    "DECIMAL_DIGITS_SPREAD": "9",
                    "DECIMAL_DIGITS_SYMVAR_TABLE": "9",
                    "DECIMAL_DIGITS_TICS": "0",
                    "DECIMAL_DIGITS_TRIGGER_VAL": "9",
                    "DECIMAL_DIGITS_WAL": "9",
                    "DECIMAL_DIGITS_WAVG_INTEGER": "9",
                    "DECIMAL_DIGITS_YIELD": "9",
                    "EXCLUDE_PREFUND_FROM_TERMS": "1",
                    "FORMAT_DURATION_AS_INTEGER": "1",
                    "MAX_SCHED_ELEMENTS": "ALL",
                    "PRICE_TICS_DECIMAL": "DECIMAL",
                    "VALID_DATES_ONLY": "1"
                },
                "CASE_SENITIVE": {

                }
            }
        },
        "requestedFields": {}
    }]

    # Call the server with the request
    resp = requests.post('http://api.apsec.com/rest/intex/v2/call',
                         data=json.dumps(task),
                         headers={'Content-Type': 'application/json'})

    deal_current = resp.json()[0]['result']

    with open(json_dump_file, 'w+') as file:
        json.dump(resp.json(), file, indent=4, sort_keys=True)

    task = [{
        "function": "DEAL_INFO",
        "params": {
            "INIT": {
                "DEFAULT": {
                    "KEYVAL_DELIM_ASCII": "10"
                },
                "CASE_SENITIVE": {

                }
            },
            "DEAL_HANDLE": {
                "DEFAULT": {
                    "ADDITIONAL_REQUIRED_ASSET_INFOS": "INTEXCALC_REIN_OVR_ID|",
                    "ADDL_MBSPOOL_FILES": "GEO",
                    "ADDL_MBSPOOL_INFO_FOR_REMICS": "0",
                    "ALLOW_ACCESS_KNOWN_CF_NMON": "FROM_SCHEDULED_PAYDATE",
                    "ALLOW_REREMIC_CHILD_CF_ACCESS": "REFERRED_CHILD_DEAL_ONLY",
                    "CDU_LOOKBACK_LIMIT_MODE": "NONE",
                    "COLLAT_LIST_TOP_LEVEL": "1",
                    "CUSIP_TABLES": "CMO|ISIN|CSI|DUS|MGP|MBS|BBGTK|BBGDEAL|BBGID|BDC",
                    "DECIMAL_DIGITS_CF_GAP": "2",
                    "DECIMAL_DIGITS_CF_TABLE": "9",
                    "DECIMAL_DIGITS_CONVEX": "9",
                    "DECIMAL_DIGITS_COUP_FAC": "9",
                    "DECIMAL_DIGITS_CP": "9",
                    "DECIMAL_DIGITS_DEC_TABLE": "0",
                    "DECIMAL_DIGITS_DISCOUNTMARGIN": "9",
                    "DECIMAL_DIGITS_DURN": "9",
                    "DECIMAL_DIGITS_FACTOR": "9",
                    "DECIMAL_DIGITS_PERCENT": "9",
                    "DECIMAL_DIGITS_PRICE": "9",
                    "DECIMAL_DIGITS_SPREAD": "9",
                    "DECIMAL_DIGITS_SYMVAR_TABLE": "9",
                    "DECIMAL_DIGITS_TICS": "0",
                    "DECIMAL_DIGITS_TRIGGER_VAL": "9",
                    "DECIMAL_DIGITS_WAL": "9",
                    "DECIMAL_DIGITS_WAVG_INTEGER": "9",
                    "DECIMAL_DIGITS_YIELD": "9",
                    "DO_EXPLODE_MEGAS": "0",
                    "DO_FORMAT_TRIGVALS": "1",
                    "EXCLUDE_PREFUND_FROM_TERMS": "1",
                    "EXTENSIVE_ERROR_CHECKING": "FATAL",
                    "FORMAT_DURATION_AS_INTEGER": "1",
                    "FULL_CASHFLOW_DETAIL": "FULL",
                    "GET_ABS_SUMMARY_FROM_LATEST_CDU": "1",
                    "GET_CHILD_TRIGGERS": "1",
                    "HIDE_MODELING_TRANCHES": "0",
                    "HIDE_RESTRICTED_TRANCHES": "1",
                    "IGNORE_DESCRIPTIVE_INFO": "NONE",
                    "IGNORE_PAIDDOWN_COLLAT": "1",
                    "INCLUDE_PNOTES": "1",
                    "INCLUDE_UNDEFINED_ASSET_INFOS": "1",
                    "LOANS_CONTROLS_LIMIT": "0",
                    "MAKE_XRS_TRANCHE": "1",
                    "MAX_SCHED_ELEMENTS": "ALL",
                    "MAX_THREADS": "8",
                    "N_PREDEFINED_VARS": "3",
                    "PNOTE_MAIN_AS_COLLAT": "0",
                    "PREDEFINED_VAR[1]": "#_IGNORE_INFO_ONLY_CDU_AS_LATEST_CDU",
                    "PREDEFINED_VAR[2]": "#EDWCOLLAT_FORCE_USE_CLUSTER_SECTION",
                    "PREDEFINED_VAR[3]": "#_LANG_FORCE_ENGLISH",
                    "PRICE_TICS_DECIMAL": "DECIMAL",
                    "REPORT_INDEX_LISTS_TO_RUN_WITH_PROXY": "1",
                    "REQUIRE_CLEANUP_PRECISION": "0",
                    "SHOW_GROUP_NAMES": "1",
                    "SHOW_HEDGE_TRANCHES": "HEDGENET",
                    "SHOW_INTERNAL_DATA_ITEMS": "1",
                    "SHOW_PSEUDO_TRANCHES": "1",
                    "SINGLE_TRANCHE_MODE": "1",
                    "STRUCTURED_ASSET_DATA_PREFERRED_SOURCE": "INTEX_DETERMINED",
                    "TAG_TRANCHE_WITH_PROVIDED_IDENTIFIER": "1",
                    "TRADING_ACCURACY_NOT_REQUIRED": "1",
                    "USE_DUEBILL": "ZERO_DELAY_BONDS",
                    "USE_HIST_ALL": "ASOFDATE_BASE_ONLY",
                    "USE_VINDEX0": "0",
                    "VALID_DATES_ONLY": "1",
                    "YLDCRV_NODES": "COMMON|1YR|3YR|7YR"
                },
                "CASE_SENITIVE": {
                    "ACCESS_CLIENT": "AMHERST INSIGHTLABS, LLC - AMHERST PIERPONT SECURITIES",
                    "ACCESS_KEYCODE": api_key,
                    "CDI_PATH": "/mnt/intexshare/intex/cmo_cdi",
                    "CDU_PATH": "/mnt/intexshare/intex/cmo_cdu"
                }
            },
            "DEAL_OPTIONS": {
                "DEFAULT": {
                    "DEAL_NAME": deal_name,
                    "DEAL_MODE": "SEASONED_POOLS",
                    "DO_OPTIMIZE_CLUSTERING": "0",
                    "DO_STRAT_COLLAT": "0",
                    "FACE_AMOUNT_SCALE_BASIS": "SUGGESTED_BAL",
                    "PARSE_CONTROL": "TYPICAL",
                    "SETTLE_YYYYMMDD": settle_date_prior
                },
                "CASE_SENITIVE": {

                }
            },
            "DEAL_INFO": {
                "DEFAULT": {
                    "DEAL_INFO_DEALNAME": deal_name,
                    "DEAL_INFO_TRANCHENAME": "COLLAT",  # defaults all info to deal level stats
                    "DECIMAL_DIGITS_CF_GAP": "2",
                    "DECIMAL_DIGITS_CF_TABLE": "9",
                    "DECIMAL_DIGITS_CONVEX": "9",
                    "DECIMAL_DIGITS_COUP_FAC": "9",
                    "DECIMAL_DIGITS_CP": "9",
                    "DECIMAL_DIGITS_DEC_TABLE": "0",
                    "DECIMAL_DIGITS_DISCOUNTMARGIN": "9",
                    "DECIMAL_DIGITS_DURN": "9",
                    "DECIMAL_DIGITS_FACTOR": "9",
                    "DECIMAL_DIGITS_PERCENT": "9",
                    "DECIMAL_DIGITS_PRICE": "9",
                    "DECIMAL_DIGITS_SPREAD": "9",
                    "DECIMAL_DIGITS_SYMVAR_TABLE": "9",
                    "DECIMAL_DIGITS_TICS": "0",
                    "DECIMAL_DIGITS_TRIGGER_VAL": "9",
                    "DECIMAL_DIGITS_WAL": "9",
                    "DECIMAL_DIGITS_WAVG_INTEGER": "9",
                    "DECIMAL_DIGITS_YIELD": "9",
                    "EXCLUDE_PREFUND_FROM_TERMS": "1",
                    "FORMAT_DURATION_AS_INTEGER": "1",
                    "MAX_SCHED_ELEMENTS": "ALL",
                    "PRICE_TICS_DECIMAL": "DECIMAL",
                    "VALID_DATES_ONLY": "1"
                },
                "CASE_SENITIVE": {

                }
            }
        },
        "requestedFields": {}
    }]

    # Call the server with the request
    resp = requests.post('http://api.apsec.com/rest/intex/v2/call',
                         data=json.dumps(task),
                         headers={'Content-Type': 'application/json'})

    deal_prior = resp.json()[0]['result']

    latest_cdu_date = deal_current["DEAL"]["LATEST_CDU_DATE"]
    current_deal = deal_current["DEAL"]["DEAL_NAME"]
    current_balance = float(deal_current["DEAL_INFO"]["TR_CURBAL"])
    prior_balance = float(deal_prior["DEAL_INFO"]["TR_CURBAL"])
    current_cdu_date = deal_current["DEAL_INFO"]["TR_CDU_PAYMENT_DATE"]
    prior_cdu_date = deal_prior["DEAL_INFO"]["TR_CDU_PAYMENT_DATE"]
    if deal_current["DEAL"].get("DEAL_PAID_DOWN_DATE") is not None:
        deal_paid_down_date = deal_current["DEAL"]["DEAL_PAID_DOWN_DATE"]
    else:
        deal_paid_down_date = None

    if deal_paid_down_date is None:
        if latest_cdu_date[:6] == settle_date[:6]:
            deal_update_status = 'Updated'
        else:
            deal_update_status = 'Not Updated'
    else:
        deal_update_status = 'Called'

    if deal_paid_down_date is None and prior_balance > 1000000:
        if current_balance < 100:
            deal_call_status = 'Called'
        elif current_balance >= 100:
            deal_call_status = 'Outstanding'
    else:
        deal_call_status = 'Paid Down'

    all_data.append({"deal_name": current_deal, "current_cdu_date": current_cdu_date, "prior_cdu_date": prior_cdu_date, "current_balance": current_balance, "prior_balance": prior_balance, "deal_update_status": deal_update_status, "deal_status": deal_call_status})
    print(deal_name)

    # 'TR_PAID_DOWN_AT_LATEST_CDU' (97863200)
with open(deal_output_path, "w+") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["deal_name", "current_cdu_date", "prior_cdu_date", "current_balance", "prior_balance", "deal_update_status", "deal_status"], lineterminator='\n', delimiter=',')
    writer.writeheader()  # uses fieldnames set above
    writer.writerows(all_data)


def test_connection():
    load_dotenv()
    api_key = os.environ.get("ACCESS_KEYCODE")
    if len(api_key) > 1:
        return "Success"
    else:
        return "Fail"


