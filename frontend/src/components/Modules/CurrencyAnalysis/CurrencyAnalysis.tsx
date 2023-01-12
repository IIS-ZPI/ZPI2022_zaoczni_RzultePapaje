import React, { useState } from 'react'
import { Bar } from 'react-chartjs-2';
import Button from '../../Button/Button';
import CurrencyPicker from '../../CurrencyPicker/CurrencyPicker';

const CurrencyAnalysis = () => {

    const [currencyCode, setCurrencyCode] = useState<string>("PLN")
    const [labelName, setLabelName] = useState<string>("");
    const [currencyData, setCurrencyData] = useState<number[]>([]);
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
    const labels = ['Spadek', 'Bez zmian', 'Wzrost'];
    const data = {
        labels,
        datasets: [
          {
            label: `${labelName}`,
            data: currencyData,
            backgroundColor: ['#FA4E4E', '#4EB3FF', '#1DC14E'],
          }
        ],
    };

    const timePeriodName = ['Tydzień', '2 Tygodnie', 'Miesiąc', 'Kwartał', '6 Miesięcy', 'Rok']

    const renderTimePeriodButton = () => {
        return (
            <div className='min-w-[90%] overflow-auto overflow-y-hidden flex justify-center'>
                {timePeriodName.map((item, index) => {
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
                            <div className={`font-medium text-xs sm:text-base ${selectedTime === index ? 'text-white' : 'text-blue-500'}`}>{item}</div> 
                        </button>
                    )
                })}
            </div>
        )
    }

    const changeSelectedTime = (value: number) => {
        setSelectedTime(value);
    }

    

    const fetchData = () => {
        setCurrencyData([12,3,56]);
        setLabelName(currencyCode)
    }

    const changeCurrency = (currencyCode: string) => {
        setCurrencyCode(currencyCode);
    }

    // useEffect(() => {
    //     fetchData();
    // }, [])

    return (
        <>
        <div className='flex items-center my-[50px]'>
            <div className='w-[100%] h-[2px] bg-gradient-to-r from-[#F2F3F4] to-gray-500 ml-[50px] mr-[10px]'></div>
            <span className='text-2xl w-[500px] text-center'>Analiza waluty</span>
            <div className='w-[100%] h-[2px] bg-gradient-to-l from-[#F2F3F4] to-gray-500 mr-[50px] ml-[10px]'></div>
        </div>

        <div className='grid lg:grid-cols-3 grid-cols-1 mt-[40px]'>
            <div className='lg:col-span-2 col-span-1 lg:row-start-1 row-start-0 mx-[40px] h-[500px] bg-white p-[80px] rounded-lg shadow'>
                    <div className='flex justify-center mb-[20px]'>
                        {renderTimePeriodButton()}
                    </div>
                <Bar options={options} data={data}/>
            </div>
            <div className='flex justify-center row-start-1 lg:row-start-0  mb-[30px]'>
                <div className='bg-white w-[85%] max-h-[175px] p-[10px] pb-[20px] rounded-lg shadow flex  flex-col items-center'>
                    <div className='mb-[10px] text-lg font-medium'>Wybierz walutę</div>
                    <div className='flex justify-center lg:flex-col sm:flex-row flex-col items-center'>
                        <CurrencyPicker countryCode='PLN' onChange={(c) => changeCurrency(c)}/>
                    </div>
                    <Button text='Sprawdź' onClick={fetchData}/>
                </div>
            </div>
        </div>
        </>
    )
}

export default CurrencyAnalysis