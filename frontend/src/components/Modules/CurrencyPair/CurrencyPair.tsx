import React, { useState } from 'react'
import { Bar } from 'react-chartjs-2'
import "chart.js/auto";
import Button from '../../Button/Button'
import CurrencyPicker from '../../CurrencyPicker/CurrencyPicker'

const CurrencyPair = () => {
    const [currencyPair, setCurrencyPair] = useState<string[]>(["PLN", "GBP"])
    const [labelName, setLabelName] = useState<string>("");
    const [labels, setLabels] = useState<string[]>(["-2", "-1", "0", '1', "2"]);
    const [currencyPairData, setCurrencyPairData] = useState<number[]>([12,45,65,32,34]);
    const [selectedTime, setSelectedTime] = useState<number>(0);

    const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'top' as const,
          },
          title: {
            display: false
          },
        },
        scales:{
            y: {
              grid:{
                  display: false
              },
            },
            x: {
              grid:{
                  display: false
              }
            }       
        }
    }

    const data = {
        labels,
        datasets: [
          {
            label: `${labelName}`,
            data: currencyPairData,
            backgroundColor: 'rgba(0, 129, 251, 0.8)',
          }
        ],
    };


    const fetchData = () => {
        setLabels(['-2', '-1', '0', '1', '2']);
        setCurrencyPairData([12,23,34,56,67]);
        setLabelName(`${currencyPair[0]}/${currencyPair[1]}`)
    }

    const changeCurrency = (currencyCode: string, index: number) => {
        const newCurrencyPair = [...currencyPair];
        newCurrencyPair[index] = currencyCode;
        setCurrencyPair(newCurrencyPair);
    }

    const changeSelectedTime = (value: number) => {
        setSelectedTime(value);
    }

    const timePeriodName = ['Miesiąc', 'Kwartał']

    const renderTimePeriodButton = () => {
        return (
            timePeriodName.map((item, index) => {
                return (
                    <button 
                        className={`border-[2px] border-blue-500 p-[5px] 
                                    ${index === 0 ? 'rounded-l-lg' : 'border-l-0'}
                                    ${index ===  timePeriodName.length - 1? 'rounded-r-lg' : ''}
                                    ${selectedTime === index ? 'bg-blue-500' : ''}
                                    `}
                        onClick={() => changeSelectedTime(index)}
                        key={index}
                        >
                        <div className={`font-medium ${selectedTime === index ? 'text-white' : 'text-blue-500'}`}>{item}</div> 
                    </button>
                )
            })
        )
    }

    // useEffect(() => {
    //     fetchData();
    // },[])

    return (
        <>
            <div className='flex items-center my-[50px]'>
                <div className='w-[100%] h-[2px] bg-gradient-to-r from-[#F2F3F4] to-gray-500 ml-[50px] mr-[10px]'></div>
                <span className='text-2xl w-[500px] text-center'>Analiza par walut</span>
                <div className='w-[100%] h-[2px] bg-gradient-to-l from-[#F2F3F4] to-gray-500 mr-[50px] ml-[10px]'></div>

            </div>
            <div className='grid lg:grid-cols-3 grid-cols-1 mt-[40px]'>
                <div className='lg:col-span-2 col-span-1 lg:row-start-1 row-start-0 mx-[40px] h-[500px] bg-white p-[10px] pb-[100px] rounded-lg shadow'>
                    <div className='flex justify-center mb-[20px]'>
                        {renderTimePeriodButton()}
                    </div>

                    <Bar options={options} data={data}/>
                </div>
                <div className='flex justify-center row-start-1 lg:row-start-0 mb-[30px]'>
                    <div className='bg-white w-[85%] max-h-[300px] p-[10px] pb-[20px] rounded-lg shadow flex  flex-col items-center'>
                        <div className='mb-[10px] text-lg font-medium'>Wybierz waluty</div>
                        <div className='flex justify-center lg:flex-col sm:flex-row flex-col items-center'>
                            <CurrencyPicker countryCode='PLN' onChange={(c) => changeCurrency(c, 0)}/>
                            <div className='text-sm m-[5px] text-slate-600 italic'>-oraz-</div>
                            <CurrencyPicker countryCode='GBP' onChange={(c) => changeCurrency(c, 1)}/>
                        </div>
                        <Button text='Sprawdź' onClick={fetchData}/>
                    </div>
                </div>
            </div>
        </>
    )
}

export default CurrencyPair