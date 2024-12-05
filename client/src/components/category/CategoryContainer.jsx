// import styled from 'styled-components'
import CategoryCard from '../category/CategoryCard'
import { useOutletContext } from 'react-router-dom'

function CategoryContainer() {
    const { categories } = useOutletContext
    return(
        <div>
            <Title>All Categories</Title>
            <CardContanier>
                {categories && categories.map(category => <CategoryCard key={category.id} category={category}/>)}
            </CardContanier>
        </div>
    )
}

export default CategoryContainer

