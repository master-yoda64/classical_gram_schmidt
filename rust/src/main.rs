use ndarray::*;
use ndarray_linalg::*;
use std::time::Instant;

fn get_orthogonal_vector(v: &Vec<ArrayView1<f64>>, q: &Vec<Array1<f64>>, k: &usize) -> Array1<f64> {
    let mut w: Array1<f64> = v[*k].to_owned();
    for i in 0..*k {
        let dot: f64 =  v[*k].dot(&q[i]);
        w = w - dot * &q[i as usize];
    }
    w
}

fn gram_schmidt(v: &Vec<ArrayView1<f64>>) -> Vec<Array1<f64>> {
    let mut q: Vec<Array1<f64>> = Vec::with_capacity(v.len());
    for k in 0..v.len(){
        q.push(get_orthogonal_vector(&v, &q, &k));
        q[k] = &q[k] / q[k].norm();
    }
    q
}

fn main() {
    let a: Array2<f64> = arr2(&[[1.0, 2.0, 3.0], [4.0, 6.0, 9.0], [7.0, 8.0, 5.0]]);
    let mut cols_vec: Vec<ArrayView1<f64>>  = Vec::with_capacity(a.ncols());
    for i in 0..a.ncols(){
        cols_vec.push(a.slice(s![.., i]));
    }
    let start = Instant::now();
    let q: Vec<Array1<f64>> = gram_schmidt(&cols_vec);
    let duration = start.elapsed();
    println!("Time for calculation: {:?}", duration);
    println!("result: {:?}", q);
    println!("q0 dot q1: {:?}", q[0].dot(&q[1]));
}
