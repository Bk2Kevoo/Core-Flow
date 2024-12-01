import styled from 'styled-components'
// import to where i want it to lead

function Home({productions}){
    return(
    <div>
        <Image /> 
        <ProductionContainer productions={productions} />
    </div>
    )
}

export default Home