from Caller import get_token, call_api
from Credentials import prodCredentials, uatCredentials
from Reader import read_json
import logging
import os
import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    logging.info('GFO function run')
    logging.info('Version: 1.3.1 - 13/02/25-13:21')

    data_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..', 'sampleData.json')
    )

    api_calls = [
        {
            "url": (
                "https://api.businesscentral.dynamics.com/v2.0/44ff170a-3cb4-47f4-9aa5-53209d400f6a/"
                "KCOM-PROD/api/v2.0/companies"
            ),
            "credentials": prodCredentials,
            "method": "GET",
            "body": {},
        },
        {
            "url": (
                "https://api.businesscentral.dynamics.com/v2.0/44ff170a-3cb4-47f4-9aa5-53209d400f6a/"
                "KCOM-UAT/api/gfo/datasets/v1.0/companies(a1c509a6-d5f2-ef11-9345-000d3aac129b)/customerLedgerEntries"
                "?$select=id%2CclosedAtDate%2CclosedByEntryNumber%2CcurrencyCode%2CcustomerNumber%2CcustomerPostingGroup%2Cdescription%2CdocumentDate%2CdocumentNumber%2CdocumentType%2CdueDate%2CentryNumber%2CexternalDocumentNumber%2ConHold%2Copen%2CoriginalCurrencyFactor%2CpaymentMethodCode%2CpostingDate%2Creversed%2CreversedByEntryNumber%2CreversedEntryNumber%2CsellToCustomerNumber%2CsourceCode%2CtransactionNumber%2CglobalDimension1Code%2CglobalDimension2Code%2CuserId%2CappliesToDocumentType%2CappliesToDocumentNumber%2Cpositive%2CclosedByAmount%2CappliesToId%2CjournalBatchName%2CreasonCode%2CbalanceAccountType%2CbalanceAccountNumber%2CclosedByAmountLcy%2CamountToApply%2CapplyingEntry%2CpaymentReference%2CappliesToExtDocumentNumber%2CpaymentTermsCode%2CsystemCreatedAt%2CsystemModifiedAt%2Camount%2CamountLCY%2CoriginalAmount%2CoriginalAmountLCY%2CremainingAmount%2CremainingAmountLCY&$filter=systemModifiedAt%20gt%202024-03-12T15%3A00%3A17.0Z&$skiptoken=89280,'AP6631601'"
            ),
            "credentials": uatCredentials,
            "method": "GET",
            "body": {},
        },
        {
            "url": (
                "https://api.businesscentral.dynamics.com/v2.0/44ff170a-3cb4-47f4-9aa5-53209d400f6a/"
                "KCOM-PROD/api/gfo/integration/v1.0/companies(85be885b-2732-f011-9a4a-7c1e52276d68)/customerActions(0)/Microsoft.NAV.customerFinancialDetails"
            ),
            "credentials": prodCredentials,
            "method": "POST",
            "body": read_json(data_path),
        },
        {
            "url": (
                "https://api.businesscentral.dynamics.com/v2.0/44ff170a-3cb4-47f4-9aa5-53209d400f6a/"
                "KCOM-PROD/api/gfo/datasets/v1.0/companies(a1c509a6-d5f2-ef11-9345-000d3aac129b)/customerLedgerEntries"
                "?$select=id%2CclosedAtDate%2CclosedByEntryNumber%2CcurrencyCode%2CcustomerNumber%2CcustomerPostingGroup%2Cdescription%2CdocumentDate%2CdocumentNumber%2CdocumentType%2CdueDate%2CentryNumber%2CexternalDocumentNumber%2ConHold%2Copen%2CoriginalCurrencyFactor%2CpaymentMethodCode%2CpostingDate%2Creversed%2CreversedByEntryNumber%2CreversedEntryNumber%2CsellToCustomerNumber%2CsourceCode%2CtransactionNumber%2CglobalDimension1Code%2CglobalDimension2Code%2CuserId%2CappliesToDocumentType%2CappliesToDocumentNumber%2Cpositive%2CclosedByAmount%2CappliesToId%2CjournalBatchName%2CreasonCode%2CbalanceAccountType%2CbalanceAccountNumber%2CclosedByAmountLcy%2CamountToApply%2CapplyingEntry%2CpaymentReference%2CappliesToExtDocumentNumber%2CpaymentTermsCode%2CsystemCreatedAt%2CsystemModifiedAt%2Camount%2CamountLCY%2CoriginalAmount%2CoriginalAmountLCY%2CremainingAmount%2CremainingAmountLCY&$filter=systemModifiedAt%20gt%202024-03-12T15%3A00%3A17.0Z&$skiptoken=89280,'AP6631601'"
            ),
            "credentials": prodCredentials,
            "method": "GET",
            "body": {},
        },
    ]

    for api in api_calls:
        token = get_token(api["credentials"])
        logging.info(f"Calling URL: {api['url']}")
        logging.info(
            call_api(
                api["url"],
                token,
                api["method"],
                api["body"],
            )
        )
