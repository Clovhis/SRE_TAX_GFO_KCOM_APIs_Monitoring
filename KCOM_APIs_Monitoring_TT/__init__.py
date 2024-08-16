from Caller import get_token,call_api
from Credentials import prodCredentials, uatCredentials
import logging
import azure.functions as func
from Reader import read_json

def main(mytimer: func.TimerRequest) -> None:
    logging.info('GFO function run')

    #Version 1.2
    logging.info('Version: 1.2.1 - 16/08/24-17:38:00')
    url = "https://gfoapi.ey.com/nav/bcapi/client-kcom/GFO180-EYGS/api/v2.0/companies"
    logging.info(call_api(url,get_token(prodCredentials),prodCredentials,"GET",{}))
    
    url = "https://gfoapiu.ey.com/navbsc/bcapi/client-kcom/GFO180-EYGS/api/gfo/datasets/v1.0/companies(284622a5-71dd-ee11-a875-000d3ab96966)/customerLedgerEntries?$select=id%2CclosedAtDate%2CclosedByEntryNumber%2CcurrencyCode%2CcustomerNumber%2CcustomerPostingGroup%2Cdescription%2CdocumentDate%2CdocumentNumber%2CdocumentType%2CdueDate%2CentryNumber%2CexternalDocumentNumber%2ConHold%2Copen%2CoriginalCurrencyFactor%2CpaymentMethodCode%2CpostingDate%2Creversed%2CreversedByEntryNumber%2CreversedEntryNumber%2CsellToCustomerNumber%2CsourceCode%2CtransactionNumber%2CglobalDimension1Code%2CglobalDimension2Code%2CuserId%2CappliesToDocumentType%2CappliesToDocumentNumber%2Cpositive%2CclosedByAmount%2CappliesToId%2CjournalBatchName%2CreasonCode%2CbalanceAccountType%2CbalanceAccountNumber%2CclosedByAmountLcy%2CamountToApply%2CapplyingEntry%2CpaymentReference%2CappliesToExtDocumentNumber%2CpaymentTermsCode%2CsystemCreatedAt%2CsystemModifiedAt%2Camount%2CamountLCY%2CoriginalAmount%2CoriginalAmountLCY%2CremainingAmount%2CremainingAmountLCY&$filter=systemModifiedAt%20gt%202024-03-12T15%3A00%3A17.0Z&$skiptoken=89280,'AP6631601'"
    logging.info(call_api(url,get_token(uatCredentials),uatCredentials,"GET",{}))
    
    url = "https://gfoapi.ey.com/nav/bcapi/client-kcom/GFO180-EYGS/api/gfo/integration/v1.0/companies(478df089-dff3-ee11-a85b-000d3ab576d1)/customerActions(0)/Microsoft.NAV.customerFinancialDetails"
    logging.info(call_api(url,get_token(prodCredentials),prodCredentials,"GET",read_json("sampleData.json")))