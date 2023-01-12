import React, { useEffect, useState } from 'react'
import { Currency, currencyData } from '../../util/CurrencyData';
import CountryFlag from '../CountryFlag/CountryFlag'

interface props{
    countryCode?: string,
    onChange?: (currency: string) => void
}

const CurrencyPicker = (props: props) => {
    const [inputText, setInputText] = useState<string>("");
    const [filteredCurrency, setFilteredCurrency] = useState<Currency[]>([]);
    const [selectedCurrency, setCurrency] = useState<Currency>();
    const [isOpen, setOpen] = useState<boolean>(false);


    const renderFilteredCurrency = () => {
        return (
            filteredCurrency.map((item, index) => {
                return (
                    <button 
                        className='h-[60px] w-[100%] flex items-center select-none hover:bg-gray-100' 
                        key={index}
                        onMouseDown={(e) => selectCurrency(item)}
                        >
                        <div className='ml-[20px]'>
                            <CountryFlag countryCode={item.Country} size={40}/>
                        </div>
                        <div className='text-left ml-[10px]'>
                            <div className='text-base font-medium'>{item.CurrencyCode}</div> 
                            <div className='text-xs text-gray-600'>{item.CurrencyName}</div>
                        </div>
                    </button>
                )
            })
        )
    }

    const selectCurrency = (item: Currency) => {
        setCurrency(item);
        toggleList();
    }

    const onChange = (e: React.FormEvent<HTMLInputElement>) => {
        const newText = e.currentTarget.value
        setInputText(newText);

        const newCurrencyList = currencyData.filter(item => {
            return item.Country.toUpperCase().startsWith(newText.toUpperCase()) 
                    || item.CurrencyCode.toUpperCase().startsWith(newText.toUpperCase()) 
                    || item.CurrencyName.toUpperCase().startsWith(newText.toUpperCase());
        })

        setFilteredCurrency(newCurrencyList);
    }

    const onBlur = () => {
        toggleList();
    }

    const toggleList = () => {
        setOpen(!isOpen);
        setInputText("");
        setFilteredCurrency(currencyData);
    }

    useEffect(() => {
        setFilteredCurrency(currencyData);
        const foundCurrency = currencyData.find(item => item.CurrencyCode === "PL")
        setCurrency({
            Country: foundCurrency?.Country || "PL",
            CurrencyName: foundCurrency?.CurrencyName || "Złoty",
            CurrencyCode: foundCurrency?.CurrencyCode || "PLN"
        })
    }, []);

    return (
        <div>
            <button 
                className='border-[2px] bg-white border-stone-300 h-[60px] min-w-[200px] rounded-md flex items-center select-none'
                onClick={toggleList}
                >
                <div className='ml-[10px]'>
                    <CountryFlag countryCode={selectedCurrency?.Country || "PL"}/>
                </div>
                <div className='text-left ml-[10px]'>
                    <div className='text-base font-medium'>{selectedCurrency?.CurrencyCode || "PLN"}</div> 
                    <div className='text-xs text-gray-600'>{selectedCurrency?.CurrencyName || "ZŁoty"}</div>
                </div>
            </button>

            {isOpen && <div className='absolute w-[250px] rounded-md shadow-md border-[1px] bg-white z-[99999]'>
                <label className="relative block">
                    <span className="sr-only">Search</span>
                    <span className="absolute inset-y-0 left-0 flex items-center pl-2">
                        <svg className="h-5 w-5 fill-slate-300" viewBox="0 0 20 20"></svg>
                    </span>
                    <input 
                        className="placeholder:italic placeholder:text-slate-400 block w-full py-2 pl-9 pr-3 shadow-sm focus:outline-none sm:text-sm" 
                        placeholder="Wpisz walute..." 
                        type="text" 
                        name="search"
                        onChange={onChange}
                        value={inputText}
                        autoFocus
                        onBlur={onBlur}
                        />
                </label>

                <div className='w-[250px] overflow-scroll overflow-x-hidden' style={{height: `${Math.min(5 * 60, filteredCurrency.length * 60)}px`}}>
                    {renderFilteredCurrency()}
                </div>
            </div>}
        </div>
    )
}

export default CurrencyPicker