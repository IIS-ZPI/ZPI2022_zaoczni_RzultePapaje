import React from 'react'
import ReactCountryFlag from 'react-country-flag'

interface props {
    countryCode?: string,
    size?: Number
}

const CountryFlag = ({countryCode = "US", size = 40}: props) => {
  return (
        <div className={`rounded-[50%] border border-stone-300 overflow-hidden shadow-md shadow-slate-400`} style={{width: `${size}px`, height: `${size}px`}}>
            <ReactCountryFlag 
                countryCode={countryCode} 
                svg
                style={{
                    width: `${size}px`,
                    height: `${size}px`,
                    transform: 'scale(1.4)'
                    }}
            />
        </div>
  )
}

export default CountryFlag