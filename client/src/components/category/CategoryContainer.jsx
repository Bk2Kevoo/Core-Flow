import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

function Category() {
  const [categories, setCategories] = useState([]);
  const { categoryId } = useParams

  useEffect(() => {
    (async () => {
        const resp = await fetch("api/v1/categories")
        const data = await resp.json()
        if (resp.ok) {
            setCategories(data)
        } else {
            toast.error(data.error)
        }
        })()
  }, [categoryId])

  return (
    <section className="container">
      {categories.map((category) => (
        <div key={category.id} className="card">
          <h2>
            {/* This link could probably be changed to populate all exercises or work exercises within this category */}
            <Link to={`/categories/${category.id}`}>{category.name}</Link>
          </h2>
          <p>Category</p>
          {/* <button onClick={() => handleDelete(category.id)}>Delete</button> */}
        </div>
      ))}
    </section>
  );
}