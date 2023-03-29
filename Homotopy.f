open System.Numerics

// Define a function that calculates the winding number of a curve in the complex plane
let windingNumber (curve: Complex -> Complex) (z: Complex) =
    let pi2 = 2.0 * Math.PI
    let x = curve
    let y = fun t -> (z - x(t)) / (z - x(t) + Complex.ImaginaryOne * 1e-10) // small perturbation to avoid singularities
    let phases = Seq.init 100 (fun i -> y(pi2 * float i / 100.0))
                    |> Seq.map (fun p -> Complex.Atan2(p.Imaginary, p.Real))
    (phases |> Seq.pairwise |> Seq.map (fun (a, b) -> (b - a + pi2) % pi2 - Math.PI)
            |> Seq.sum) / Math.PI

// Define a function that calculates the curvature of a curve in the complex plane
let curvature (curve: Complex -> Complex) (t: float) =
    let z = curve(t)
    let dz = curve(t + 0.0001) - z
    let ddz = curve(t + 0.0002) - 2.0 * dz + z
    Complex.Abs(dz) * Complex.Abs(ddz) / Complex.Pow(dz, 3.0)

// Define a function that calculates the Gaussian curvature of a surface in three-dimensional space
let gaussianCurvature (surface: float -> float -> Vector3) (u: float, v: float) =
    let du = surface(u + 0.0001, v) - surface(u, v)
    let dv = surface(u, v + 0.0001) - surface(u, v)
    let n = Vector3.Cross(du, dv)
    let e = Vector3.Dot(du, du) * Vector3.Dot(dv, dv) - Vector3.Dot(du, dv) ** 2.0
    - Vector3.Dot(n, n) / e

// Define a function that calculates the mean curvature of a surface in three-dimensional space
let meanCurvature (surface: float -> float -> Vector3) (u: float, v: float) =
    let du = surface(u + 0.0001, v) - surface(u, v)
    let dv = surface(u, v + 0.0001) - surface(u, v)
    let n = Vector3.Cross(du, dv)
    let e = Vector3.Dot(du, du) * Vector3.Dot(dv, dv) - Vector3.Dot(du, dv) ** 2.0
    let f = Vector3.Dot(surface(u, v), n)
    (Vector3.Dot(n, Vector3.Cross(du, n)) / e + Vector3.Dot(n, Vector3.Cross(dv, n)) / e) / 2.0 - f / e

// Test the functions using sample curves and surfaces
let c1 t = Complex.Create(Math.Cos(t), Math.Sin(t))
let c2 t = Complex.Create(Math.Cos(2.0 * t), Math.Sin(3.0 * t))
let s1 u v = Vector3.Create((Math.Cos(u) * Math.Cos(v)), (Math.Sin(u) * Math.Cos(v)), Math.Sin(v))
let s2 u v = Vector3.Create((Math.Cos(u
