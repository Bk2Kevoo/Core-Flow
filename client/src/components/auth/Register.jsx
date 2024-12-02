import { useState, useEffect } from "react";
import { object, string } from "yup";
import { Formik } from "formik";
import styled from "styled-components";
import toast from "react-hot-toast";
import { useOutletContext, useNavigate } from "react-router-dom";

const signupSchema = object ({
    name: string("name must be of type string")
        .min(3, "name must be 3 characters or more")
        .required("name is required"),
    email: string("email must be of type string")
        .email("email must be valid")
        .max(40, "email must be 40 characters max")
        .required("email is required"),
    password: string("password must be of type string")
        .min(8, "password has to be at least 8 characters long")
        .max(20, "password must be 20 characters long max")
        .required("password is required")
});

const signinSchema = object({
    email: string("email has to be a string")
      .email("email must be valid")
      .max(40, "email must be 40 characters max")
      .required("email is required"),
    password: string("password has to be a string")
      .min(8, "password has to be at least 8 characters long")
      .max(20, "password must be 20 characters long max")
      .required("password is required"),
  });

const initialValues = {
    name: "",
    email: "",
    password: "",
  }
  
const Registration = () => {
    const [isLogin, setIsLogin] = useState(true);
    const { currentUser, updateUser } = useOutletContext();
    const navigate = useNavigate();
  
    useEffect(() => {
      if (currentUser) {
        navigate("/");
      }
    }, [currentUser, navigate]);

    return (
        <div>
            <h2>Log in or Sign Up</h2>
            <h3>{isLogin ? "Not a Member?": "Already a Member?"}</h3>
            <button onClick={() => setIsLogin((current) => !current)}>
                {isLogin ? "Register Here!": "Login!"}
            </button>
            <Formik>
                initialValues={initialValues}
                onSubmit={async (values) => {
                    const url = isLogin ? "api/v1/login" : "api/v1/signup"
                    const response = await fetch(url, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                            "Accept": "application/json",
                        },
                        body: JSON.stringify(values)
                    });
                    const data = await response.json()
                    if (response.ok) {
                        toast.success(
                            isLogin
                            ? `Welcome back, ${data.username}`
                            : `Welcome, ${data.username}`
                        );
                        updateUser(data);
                        navigate("/")
                    } else {
                        toast.error(data.error)
                    }
                }}
                validationSchema={isLogin ? signinSchema : signupSchema}
                {({
                handleBlur,
                handleChange,
                handleSubmit,
                values,
                errors,
                touched,
                isSubmitting,
        }) => (
          <Form onSubmit={handleSubmit}>
            {!isLogin && (
              <>
                <label htmlFor="username">Username</label>
                <input
                  type="text"
                  name="username"
                  onChange={handleChange}
                  onBlur={handleBlur}
                  value={values.username}
                />
                {errors.username && touched.username && (
                  <div className="error-message show">{errors.name}</div>
                )}
              </>
            )}
            <label htmlFor="email">Email</label>
            <input
              type="email"
              name="email"
              onChange={handleChange}
              onBlur={handleBlur}
              value={values.email}
            />
            {errors.email && touched.email && (
              <div className="error-message show">{errors.email}</div>
            )}

            <label htmlFor="password">Password</label>
            <input
              type="password"
              name="password"
              onChange={handleChange}
              onBlur={handleBlur}
              value={values.password}
            />
            {errors.password && touched.password && (
              <div className="error-message show">{errors.password}</div>
            )}

            <input
              type="submit"
              value={isLogin ? "Login!" : "Create Account!"}
            />
          </Form>
        )}
      </Formik>
    </div>
  );
};

export default Registration;