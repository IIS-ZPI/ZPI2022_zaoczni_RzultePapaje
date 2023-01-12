import React from 'react'
import CountryFlag from '../CountryFlag/CountryFlag'

const CurrencyPicker = () => {
  return (
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
  )
}

export default CurrencyPicker