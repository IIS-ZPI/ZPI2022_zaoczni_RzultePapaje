import React from 'react'
import CurrencyAnalysis from '../../components/Modules/CurrencyAnalysis/CurrencyAnalysis'
import CurrencyPair from '../../components/Modules/CurrencyPair/CurrencyPair'


const Home = () => {
  return (
        <>
            <CurrencyPair/>
            <CurrencyAnalysis/>
        </>
    )
}

export default Home