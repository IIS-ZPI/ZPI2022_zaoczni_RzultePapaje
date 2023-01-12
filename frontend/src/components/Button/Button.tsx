interface props {
    text: string,
    onClick?: () => void
}

const Button = ({text, onClick}: props) => {
    return (
        <button 
            className='bg-blue-500 p-[5px] min-w-[100px] rounded-md mt-[20px]'
            onClick={onClick}
            >
            <div className='text-white text-sm'>
                {text}
            </div>
        </button>
    )
}

export default Button