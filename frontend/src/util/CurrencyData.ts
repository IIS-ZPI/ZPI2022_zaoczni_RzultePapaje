export interface Currency {
    Country: string,
    CurrencyName: string,
    CurrencyCode: string
}

export const currencyData: Currency[] = [
    {
       "Country":"PL",
       "CurrencyName":"Polski Złoty",
       "CurrencyCode":"PLN"
    },
	{
       "Country":"DE",
       "CurrencyName":"Euro",
       "CurrencyCode":"EUR"
    },
	{
       "Country":"US",
       "CurrencyName":"Dolar amerykański",
       "CurrencyCode":"USD"
    },
	{
       "Country":"GB",
       "CurrencyName":"Funt brytyjski",
       "CurrencyCode":"GBP"
    },
	{
       "Country":"CH",
       "CurrencyName":"Frank szwajcarski",
       "CurrencyCode":"CHF"
    },
    {
        "Country":"CA",
        "CurrencyName":"Dolar kanadyjski",
        "CurrencyCode":"CAD"
    },
	{
       "Country":"CN",
       "CurrencyName":"Juan chiński",
       "CurrencyCode":"CNY"
    },
	{
       "Country":"DK",
       "CurrencyName":"Korona duńska",
       "CurrencyCode":"DKK"
    },
	{
       "Country":"JP",
       "CurrencyName":"Jen japoński",
       "CurrencyCode":"JPY"
    }
]