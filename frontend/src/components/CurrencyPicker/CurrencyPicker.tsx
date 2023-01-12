import React, { useState } from 'react'
import { Currency } from '../../util/CurrencyData';
import CountryFlag from '../CountryFlag/CountryFlag'

const CurrencyPicker = () => {
    const [inputText, setInputText] = useState<string>("");
    const [filteredCurrency, setFilteredCurrency] = useState<Currency[]>([]);
    const [selectedCurrency, setCurrency] = useState<Currency>();
    const [isOpen, setOpen] = useState<boolean>(false);


    return (
        <div>
            <button 
                className='border-[2px] border-stone-300 h-[60px] min-w-[200px] rounded-md flex items-center select-none'
                >
                <div className='ml-[10px]'>
                    <CountryFlag/>
                </div>
                <div className='text-left ml-[10px]'>
                    <div className='text-base font-medium'>{"PLN"}</div> 
                    <div className='text-xs text-gray-600'>{"ZŁoty"}</div>
                </div>
            </button>

            <div className='absolute w-[250px] rounded-md shadow-md border-[1px] bg-white z-[99999]'>
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
                        value={inputText}
                        />
                </label>
            </div>
        </div>
    )
}

export default CurrencyPicker