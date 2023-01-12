import React from 'react'
import CurrencyAnalysis from '../../components/Modules/CurrencyAnalysis/CurrencyAnalysis'
import CurrencyPair from '../../components/Modules/CurrencyPair/CurrencyPair'


const Home = () => {
  return (
        <>
            <div className='mb-[50px]'>
                <CurrencyPair/>
            </div>

            <div className='mb-[50px]'>
                <CurrencyAnalysis/>
            </div>
        </>
    )
}

export default Home