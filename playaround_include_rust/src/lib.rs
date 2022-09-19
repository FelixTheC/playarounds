use pyo3::prelude::*;
use pyo3::types::*;


fn inspect_container_element_types(container: &PyAny, required_type: &PyType) -> bool
{
    let mut result = true;
    match container.cast_as::<PyList>()
    {
        Ok(obj) =>
            {
                for element in obj.iter()
                {
                    let check = element.is_instance(required_type).unwrap();
                    if !check
                    {
                        result = false;
                        break;
                    }
                }
                result
            }
        Err(_) => result
    }
}

#[pyfunction]
fn is_type_of(a: &PyAny, b: &PyAny) -> Py<PyBool>
{
    Python::with_gil(|py| {
        let mut is_type: bool = false;

        match b.cast_as::<PyType> ()
        {
            Ok(obj) =>
                {
                    is_type = a.is_instance(obj).unwrap();
                },
            Err(_) =>
                {
                    match b.hasattr("__origin__")
                    {
                        Ok(_) =>
                            {
                                let tmp = b.getattr("__origin__")
                                    .unwrap()
                                    .cast_as::<PyType>()
                                    .unwrap();
                                is_type = a.is_instance(&tmp).unwrap();
                            },
                        Err(_) => ()
                    }
                    match b.hasattr("__args__")
                    {
                        Ok(_) =>
                            {
                                let tmp = b.getattr("__args__")
                                    .unwrap()
                                    .cast_as::<PyTuple>()
                                    .unwrap();
                                let child_types = tmp.get_item(0)
                                    .unwrap()
                                    .cast_as::<PyType>()
                                    .unwrap();
                                is_type = inspect_container_element_types(a, child_types);
                            },
                        Err(_) => ()
                    }
                }
        };

        PyBool::new(py, is_type).into()
    })
}

/// A Python module implemented in Rust.
#[pymodule]
fn include_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(is_type_of, m)?)?;
    Ok(())
}