


def torsional_stiffness():
    """
    Torsional Stiffness of the Bar (\(k_{bar}\))
    The stiffness of the anti-roll bar itself depends on the material's shear modulus, the bar's diameter, and its geometry.
    For a solid round bar, the math is:
        k_bar = pi * G * d^4 ÷ 32 * L
    Where:
        G: Shear modulus of the material (typically ≈79,300 MPa or 11,500,000 psi for spring steel)
        d: Bar diameter
        L: Lever arm length (the effective length from the bend to the end-link attachment)
        Note: Because d is raised to the 4th power, a tiny change in ARB thickness drastically changes stiffness.

    2. Motion Ratio (\(MR\))Because the ARB rarely mounts directly to the wheel hub, the force it exerts depends on where the end-link connects to the control arm.
    \(MR = \frac{\text{Distance from inner pivot to sway bar mount}}{\text{Distance from inner pivot to center of tire contact patch}}\)3. Sway Bar Wheel Rate (\(K_{wheel}\))This is the effective spring rate felt at the tire, which you actually use to calculate total vehicle roll stiffness.\(K_{wheel} = k_{bar} \times (MR)^2\)Rally-Specific Tuning ApplicationBecause rally stages feature loose gravel, dirt, and undulations, your math-based tuning needs to accommodate surface grip:Stiffer Front Bar / Softer Rear Bar: Increases front roll resistance, causing the front outside tire to take a higher percentage of the lateral weight transfer. This reduces front grip, inducing understeer (good for high-speed stability on loose straights).Softer Front Bar / Stiffer Rear Bar: Shifts weight transfer to the rear, keeping the front tires planted and reducing inside-rear lift. This promotes oversteer/rotation (essential for hairpins on tight gravel rallies).Open Diff / Rough Bumps: Very stiff bars will cause the inside tire to lift in heavy ruts or crests, losing traction. You will often calculate a much softer setting for rough, rutted stages compared to smooth tarmac events.Practical Trackside Adjustments
    :return:
    """