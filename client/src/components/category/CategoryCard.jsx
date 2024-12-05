import styled from "styled-components"
// import {Link} from "react-router-dom"4

function CategoryCard() {
    const {name, id} = category
    
    return (
        <Card id={id}>
            <Link to={`/categories/${id}`}>
                <div>
                    <h2>{name}</h2>
                </div>
            </Link>
        </Card>
    )
}

export default CategoryCard

const Card = styled.li `
    display:flex;

`