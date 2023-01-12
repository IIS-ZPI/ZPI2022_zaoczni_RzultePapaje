import React from 'react'
import Button from '../../Button/Button'
import CurrencyPicker from '../../CurrencyPicker/CurrencyPicker'

const CurrencyPair = () => {
  return (
    <>
        <div className='flex items-center my-[50px]'>
            <div className='w-[100%] h-[2px] bg-gradient-to-r from-[#F2F3F4] to-gray-500 ml-[50px] mr-[10px]'></div>
            <span className='text-2xl w-[500px] text-center'>Analiza par walut</span>
            <div className='w-[100%] h-[1px] bg-zinc-600 mr-[50px] ml-[10px]'></div>
        </div>
        <div className='grid lg:grid-cols-3 grid-cols-1 mt-[40px]'>
            <div className='lg:col-span-2 col-span-1 lg:row-start-1 row-start-0 mx-[40px] h-[500px] bg-white p-[10px] pb-[100px] rounded-lg shadow'>
            </div>
            <div className='flex justify-center row-start-1 lg:row-start-0 mb-[30px]'>
                <div className='bg-white w-[85%] max-h-[300px] p-[10px] pb-[20px] rounded-lg shadow flex  flex-col items-center'>
                    <div className='mb-[10px] text-lg font-medium'>Wybierz waluty</div>
                    <div className='flex justify-center lg:flex-col sm:flex-row flex-col items-center'>
                        <CurrencyPicker countryCode='PLN'/>
                        <div className='text-sm m-[5px] text-slate-600 italic'>-oraz-</div>
                        <CurrencyPicker countryCode='GBP'/>
                    </div>
                    <Button text='Sprawdź'/>
                </div>
            </div>
        </div>
    </>
  )
}

export default CurrencyPair