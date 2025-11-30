import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math
import random
import requests  # <-- AÑADIDO: necesario para la IA

# =============== DATOS CURIOSOS DE FÍSICA ===============
def get_random_curiosity():
    """Devuelve un dato curioso aleatorio sobre física."""
    curiosidades = [
        # Termodinámica (🔥)
        "🔥 El cero absoluto (0 K) es la temperatura más baja posible, donde toda agitación molecular se detiene. ¡Nunca se ha alcanzado en el universo!",
        "🔥 Una taza de café caliente se enfría más rápido si soplas sobre ella. Esto no solo mueve el aire, sino que también reduce la capa de vapor saturado.",
        "🔥 Los agujeros negros tienen una entropía gigantesca, proporcional al área de su horizonte de eventos, no a su volumen.",
        "🔥 El helio líquido a -271°C se convierte en un superfluido que escala las paredes de su contenedor y no tiene viscosidad.",
        "🔥 El Sol convierte 600 millones de toneladas de hidrógeno en helio cada segundo. Esa energía es la que nos da vida.",
        "🔥 La entropía siempre aumenta en un sistema aislado. Es la razón por la que el hielo se derrite y el café se enfría, nunca al revés.",
        "🔥 El fuego no es plasma en condiciones normales. Solo en temperaturas extremadamente altas (como en las estrellas) el fuego se convierte en plasma.",
        "🔥 El punto triple del agua es a 0.01°C y 611.657 Pa. Es el único punto donde el agua coexiste como sólido, líquido y gas al mismo tiempo.",
        "🔥 Un motor térmico perfecto (de Carnot) no puede existir. Siempre hay pérdidas de energía en forma de calor.",
        "🔥 La temperatura más alta jamás creada en un laboratorio es de 5.5 billones de grados Celsius (en el LHC).",
        # Electricidad y Magnetismo (⚡)
        "⚡ La electricidad viaja por los cables casi a la velocidad de la luz, pero los electrones individuales apenas se mueven (deriva).",
        "⚡ Un relámpago puede calentar el aire hasta 30,000 °C, ¡cinco veces más que la superficie del Sol!",
        "⚡ Tu cuerpo genera electricidad. Las neuronas transmiten señales usando impulsos eléctricos de iones de sodio y potasio.",
        "⚡ El campo magnético de la Tierra protege la vida desviando el viento solar. Sin él, nuestra atmósfera se habría erosionado como Marte.",
        "⚡ Si pudieras almacenar la energía de un rayo, sería suficiente para encender una bombilla de 100W durante unos 3 meses.",
        "⚡ Los imanes de neodimio son los más potentes del mundo y pueden levantar más de 1,000 veces su propio peso.",
        "⚡ La corriente alterna (AC) se usa en las redes eléctricas porque es más eficiente para transportar energía a largas distancias.",
        "⚡ El efecto Hall es usado en sensores de posición y velocidad en autos y teléfonos móviles.",
        "⚡ Un electroimán se apaga al cortar la corriente. Un imán permanente, no.",
        "⚡ La ley de Lenz dice que una corriente inducida siempre se opondrá al cambio que la produjo. Es la naturaleza diciendo 'no'.",
        "⚡ Los superconductores expulsan completamente los campos magnéticos (efecto Meissner) y permiten que imanes floten sobre ellos.",
        "⚡ La intensidad de un campo eléctrico disminuye con el cuadrado de la distancia. ¡Es una ley inversa al cuadrado, como la gravedad!",
        "⚡ Las jaulas de Faraday bloquean los campos eléctricos externos. Tu microondas es una jaula de Faraday.",
        "⚡ La resistencia eléctrica de los metales aumenta con la temperatura, pero la de los semiconductores disminuye.",
        "⚡ El primer condensador fue la 'Botella de Leyden', inventada en 1745 para almacenar electricidad estática.",
        # Óptica y Ondas (🌊)
        "🌊 La luz visible es solo una pequeña fracción del espectro electromagnético. Podemos ver menos del 0.0035% de todas las longitudes de onda.",
        "🌊 El sonido no se propaga en el vacío del espacio. ¡Los gritos en el espacio exterior no se escuchan!",
        "🌊 Los delfines y murciélagos usan ecolocalización, enviando ondas ultrasónicas y escuchando sus ecos para 'ver'.",
        "🌊 La frecuencia de la nota musical 'La' estándar es 440 Hz. Esta convención se estableció en 1939.",
        "🌊 Las olas del mar son ondas mecánicas transversales que transportan energía, no agua. El agua solo se mueve en círculos.",
        "🌊 Cuando miras una estrella, la estás viendo tal como era hace años, décadas o siglos. ¡Estás mirando hacia el pasado!",
        "🌊 Un diamante puede brillar tanto porque tiene un índice de refracción muy alto (n≈2.4), lo que significa que la luz se dobla mucho.",
        "🌊 La fibra óptica funciona gracias a la reflexión total interna. La luz queda atrapada en el núcleo de vidrio por completo.",
        "🌊 Si un objeto se mueve a la velocidad de la luz, su longitud en la dirección del movimiento se contraería a cero.",
        "🌊 El arcoíris se forma por refracción, reflexión interna y dispersión de la luz en las gotas de agua.",
        "🌊 La luz polarizada reduce el deslumbramiento. Las gafas de sol polarizadas bloquean la luz reflejada horizontalmente.",
        "🌊 El color del cielo es azul por la dispersión de Rayleigh. La luz azul se dispersa más que la roja porque tiene menor longitud de onda.",
        "🌊 El sonido viaja más rápido en el agua que en el aire, y aún más rápido en el acero.",
        "🌊 Las ondas de radio, las microondas y los rayos X son todas luz, solo que con longitudes de onda diferentes.",
        "🌊 La interferencia de ondas es lo que crea patrones de franjas en experimentos como el de Young, demostrando la naturaleza ondulatoria de la luz.",
        "🌊 El efecto Doppler no solo aplica al sonido (sirena de ambulancia), sino también a la luz (corrimiento al rojo en galaxias).",
        "🌊 Un prisma separa la luz blanca en colores porque cada color (longitud de onda) se refracta un poco diferente.",
        "🌊 La velocidad de la luz en el vacío (299,792,458 m/s) es el límite de velocidad del universo. Nada puede ir más rápido.",
        # Física Moderna y Diversos (🧠)
        "🧠 La teoría de la relatividad especial de Einstein se basa en dos postulados: la física es igual en todos los sistemas inerciales y la luz es constante.",
        "🧠 El principio de incertidumbre de Heisenberg dice que no puedes conocer con precisión la posición y la velocidad de una partícula a la vez.",
        "🧠 El efecto túnel cuántico permite a las partículas atravesar barreras imposibles. Es clave en la fusión nuclear del Sol.",
        "🧠 El LED convierte la electricidad directamente en luz sin generar casi calor, siendo mucho más eficiente que las bombillas incandescentes.",
        "🧠 El magnetron en tu microondas genera ondas que hacen vibrar las moléculas de agua en los alimentos, calentándolos.",
        "🧠 El GPS necesita correcciones relativistas. Los satélites experimentan el tiempo ligeramente más rápido que en la Tierra. ¡Sin Einstein, fallaría!",
        "🧠 La energía total del universo podría ser cero. La energía positiva de la materia podría estar equilibrada por la energía negativa de la gravedad.",
        "🧠 En mecánica cuántica, una partícula puede estar en múltiples estados a la vez (superposición) hasta que se mide.",
        "🧠 El CERN, en Suiza, es el laboratorio de física de partículas más grande del mundo. Allí se descubrió el bosón de Higgs.",
        "🧠 Un agujero de gusano es una solución teórica en la relatividad general que podría conectar dos puntos distantes del espacio-tiempo."
    ]
    return random.choice(curiosidades)
# =============== ESTILOS Y CONFIGURACIÓN ===============
st.set_page_config(
    page_title="Física Inteligente",
    page_icon="🧠",
    layout="wide"
)
# Estilos CSS mejorados
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 2rem;
    }
    .module-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-left: 4px solid #3498db;
    }
    .result-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .info-box {
        background: #f8f9fa;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    .explanation-box {
        background: #e3f2fd;
        border-left: 4px solid #2196f3;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    .warning-box {
        background: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    .error-box {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 1px solid #f5c6cb;
    }
    /* Cuadro azul en la sidebar */
    .sidebar-instructions {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
        font-size: 0.9rem;
    }
    /* Cuadro azul para dato curioso */
    .curiosity-box {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)
# =============== FUNCIONES UTILITARIAS ===============
def format_scientific(value, unit):
    """Formatea números en notación científica con unidades."""
    if value is None or math.isnan(value) or math.isinf(value):
        return "Indefinido"
    if abs(value) >= 1e5 or (abs(value) < 1e-2 and abs(value) > 0):
        return f"{value:.2e} {unit}"
    else:
        return f"{value:.4g} {unit}"
def show_emoji_header(emoji, text):
    """Muestra un encabezado con emoji"""
    st.markdown(f"### {emoji} {text}")
def show_calculation_process(formula, steps, result, unit, description=""):
    """
    Muestra el proceso de cálculo de forma clara y atractiva.
    """
    st.latex(formula)
    if steps:
        st.markdown("*Pasos del cálculo:*")
        for step in steps:
            st.code(step, language="python")
    formatted_result = format_scientific(result, unit)
    result_html = f"""
    <div class="result-box">
        <h4 style="margin:0; font-size: 1.1rem;">Resultado Final</h4>
        <p style="font-size: 1.3rem; margin: 0.5rem 0;">{formatted_result}</p>
        {f'<p style="margin:0; opacity:0.9;">{description}</p>' if description else ''}
    </div>
    """
    st.markdown(result_html, unsafe_allow_html=True)
def show_error_message(message):
    st.markdown(f'<div class="error-box">{message}</div>', unsafe_allow_html=True)
def show_warning_message(message):
    st.markdown(f'<div class="warning-box">{message}</div>', unsafe_allow_html=True)
# =============== FUNCIONES DE CÁLCULO ACTUALIZADAS ===============
def convertir_temperatura(valor, de, a):
    if de == "Celsius":
        c = valor
    elif de == "Kelvin":
        if valor < 0:
            st.error("La temperatura en Kelvin no puede ser negativa.")
            return None
        c = valor - 273.15
    elif de == "Fahrenheit":
        c = (valor - 32) * 5/9
    else:
        st.error(f"Unidad de entrada '{de}' no válida.")
        return None
    if a == "Celsius":
        res = c
    elif a == "Kelvin":
        res = c + 273.15
        if res < 0:
            st.error("La temperatura en Kelvin no puede ser negativa.")
            return None
    elif a == "Fahrenheit":
        res = c * 9/5 + 32
    else:
        st.error(f"Unidad de salida '{a}' no válida.")
        return None
    if res is not None:
        show_calculation_process(
            formula=r"T(K) = T(C) + 273.15 \quad \text{o} \quad T(F) = \frac{9}{5}T(C) + 32",
            steps=[f"Entrada: {valor}° {de}", f"Salida: {res:.2f}° {a}"],
            result=res,
            unit=f"°{a}",
            description=f"Temperatura equivalente en {a}."
        )
    return res
def calor_sensible_process(masa, c_especifico, delta_t):
    if masa <= 0 or c_especifico <= 0:
        return None
    q = masa * c_especifico * delta_t
    steps = [
        f"Q = m * c * ΔT",
        f"Q = {masa} * {c_especifico} * {delta_t}",
        f"Q = {q:.2f}"
    ]
    return q, steps, "J", "Calor absorbido o liberado por el cambio de temperatura."
def calor_latente_process(masa, l):
    if masa <= 0 or l <= 0:
        return None
    q = masa * l
    steps = [
        f"Q = m * L",
        f"Q = {masa} * {l}",
        f"Q = {q:.2f}"
    ]
    return q, steps, "J", "Calor absorbido o liberado durante un cambio de estado."
def primera_ley_termodinamica_process(delta_u, q=None, w=None):
    try:
        if q is None and w is not None:
            q_calc = delta_u + w
            steps = [
                f"Q = ΔU + W",
                f"Q = {delta_u} + {w}",
                f"Q = {q_calc:.2f}"
            ]
            return q_calc, steps, "J", "Calor transferido al sistema."
        elif w is None and q is not None:
            w_calc = q - delta_u
            steps = [
                f"W = Q - ΔU",
                f"W = {q} - {delta_u}",
                f"W = {w_calc:.2f}"
            ]
            return w_calc, steps, "J", "Trabajo realizado por el sistema."
        else:
            return None
    except Exception as e:
        return None
def ley_coulomb_process(q1, q2, r, k=8.99e9):
    if r <= 0:
        return None
    f = k * abs(q1 * q2) / r**2
    steps = [
        f"F = k * |q₁ * q₂| / r²",
        f"F = {k:.2e} * |{q1:.2e} * {q2:.2e}| / {r}²",
        f"F = {k:.2e} * {abs(q1*q2):.2e} / {r**2}",
        f"F = {f:.2e}"
    ]
    return f, steps, "N", "Fuerza de atracción o repulsión entre las cargas."
def campo_electrico_process(q, r, k=8.99e9):
    if r <= 0:
        return None
    e = k * abs(q) / r**2
    steps = [
        f"E = k * |q| / r²",
        f"E = {k:.2e} * |{q:.2e}| / {r}²",
        f"E = {k:.2e} * {abs(q):.2e} / {r**2}",
        f"E = {e:.2e}"
    ]
    return e, steps, "N/C", "Intensidad del campo eléctrico."
def potencial_electrico_process(q, r, k=8.99e9):
    if r <= 0:
        return None
    v = k * q / r
    steps = [
        f"V = k * q / r",
        f"V = {k:.2e} * {q:.2e} / {r}",
        f"V = {v:.2e}"
    ]
    return v, steps, "V", "Potencial eléctrico."
def capacitor_energia_process(c, v):
    if c < 0 or v < 0:
        return None
    u = 0.5 * c * v**2
    steps = [
        f"U = ½ * C * V²",
        f"U = 0.5 * {c:.2e} * {v}²",
        f"U = 0.5 * {c:.2e} * {v**2}",
        f"U = {u:.2e}"
    ]
    return u, steps, "J", "Energía almacenada en el capacitor."
def ley_ohm_process(v=None, i=None, r=None):
    try:
        if v is None and i is not None and r is not None:
            v_calc = i * r
            steps = [
                f"V = I * R",
                f"V = {i} * {r}",
                f"V = {v_calc:.2f}"
            ]
            return v_calc, steps, "V", "Diferencia de potencial (voltaje)."
        elif i is None and v is not None and r is not None:
            if r == 0:
                return None
            i_calc = v / r
            steps = [
                f"I = V / R",
                f"I = {v} / {r}",
                f"I = {i_calc:.2f}"
            ]
            return i_calc, steps, "A", "Corriente eléctrica."
        elif r is None and v is not None and i is not None:
            if i == 0:
                return None
            r_calc = v / i
            steps = [
                f"R = V / I",
                f"R = {v} / {i}",
                f"R = {r_calc:.2f}"
            ]
            return r_calc, steps, "Ω", "Resistencia eléctrica."
        else:
            return None
    except Exception as e:
        return None
def potencia_electrica_process(v=None, i=None, r=None):
    try:
        if v is not None and i is not None:
            p = v * i
            steps = [
                f"P = V * I",
                f"P = {v} * {i}",
                f"P = {p:.2f}"
            ]
        elif i is not None and r is not None:
            p = i**2 * r
            steps = [
                f"P = I² * R",
                f"P = {i}² * {r}",
                f"P = {i**2} * {r}",
                f"P = {p:.2f}"
            ]
        elif v is not None and r is not None:
            if r == 0:
                return None
            p = v**2 / r
            steps = [
                f"P = V² / R",
                f"P = {v}² / {r}",
                f"P = {v**2} / {r}",
                f"P = {p:.2f}"
            ]
        else:
            return None
        return p, steps, "W", "Potencia disipada o generada."
    except Exception as e:
        return None
def frecuencia_periodo_process(f=None, t=None):
    try:
        if f is None and t is not None and t != 0:
            f_calc = 1 / t
            steps = [
                f"f = 1 / T",
                f"f = 1 / {t}",
                f"f = {f_calc:.2f}"
            ]
            return f_calc, steps, "Hz", "Frecuencia de la onda."
        elif t is None and f is not None and f != 0:
            t_calc = 1 / f
            steps = [
                f"T = 1 / f",
                f"T = 1 / {f}",
                f"T = {t_calc:.4f}"
            ]
            return t_calc, steps, "s", "Período de la onda."
        else:
            return None
    except Exception as e:
        return None
def velocidad_onda_process(f, lam):
    if f < 0 or lam < 0:
        return None
    v = f * lam
    steps = [
        f"v = f * λ",
        f"v = {f} * {lam}",
        f"v = {v:.2f}"
    ]
    return v, steps, "m/s", "Velocidad de propagación de la onda."
def energia_foton_process(f=None, lam=None, h=6.626e-34, c=3e8):
    try:
        if f is not None:
            if f < 0:
                return None
            e = h * f
            steps = [
                f"E = h * f",
                f"E = {h:.2e} * {f:.2e}",
                f"E = {e:.2e}"
            ]
        elif lam is not None:
            if lam <= 0:
                return None
            e = h * c / lam
            steps = [
                f"E = h * c / λ",
                f"E = {h:.2e} * {c:.2e} / {lam:.2e}",
                f"E = {h*c:.2e} / {lam:.2e}",
                f"E = {e:.2e}"
            ]
        else:
            return None
        return e, steps, "J", "Energía de un fotón."
    except Exception as e:
        return None
def ley_snell_process(n1, angulo1, n2):
    if n1 <= 0 or n2 <= 0:
        return None
    theta1_rad = math.radians(angulo1)
    sin_theta2 = n1 * math.sin(theta1_rad) / n2
    if abs(sin_theta2) > 1:
        return None, [], "", "Reflexión total interna. La luz se refleja completamente en la interfaz."
    theta2 = math.degrees(math.asin(sin_theta2))
    steps = [
        f"n₁ * sin(θ₁) = n₂ * sin(θ₂)",
        f"{n1} * sin({angulo1}°) = {n2} * sin(θ₂)",
        f"{n1} * {math.sin(theta1_rad):.4f} = {n2} * sin(θ₂)",
        f"{n1 * math.sin(theta1_rad):.4f} = {n2} * sin(θ₂)",
        f"sin(θ₂) = {sin_theta2:.4f}",
        f"θ₂ = arcsin({sin_theta2:.4f})",
        f"θ₂ = {theta2:.2f}°"
    ]
    return theta2, steps, "°", "Ángulo de refracción."
# =============== GRÁFICOS INTERACTIVOS MEJORADOS ===============
def graficar_dilatacion_lineal_interactiva(l0, alpha, dt_max):
    if l0 <= 0 or alpha < 0 or dt_max < 0:
        return go.Figure()
    dt_vals = np.linspace(0, dt_max, 100)
    l_vals = l0 * (1 + alpha * dt_vals)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dt_vals,
        y=l_vals,
        mode='lines',
        name='Longitud',
        line=dict(color='#e74c3c', width=3)
    ))
    fig.update_layout(
        title="🌡 Dilatación Térmica Lineal",
        xaxis_title="ΔT (°C)",
        yaxis_title="Longitud L (m)",
        template="plotly_white",
        font=dict(size=12),
        title_font_size=18,
        hovermode='x unified'
    )
    return fig
def graficar_campo_electrico_interactivo(q, r, r_max=10.0):
    if r_max <= 0:
        r_max = 10.0
    r_vals = np.linspace(0.1, r_max, 200)
    k = 8.99e9
    e_vals = k * abs(q) / r_vals**2
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=r_vals,
        y=e_vals,
        mode='lines',
        name='E(r) teórico',
        line=dict(color='#3498db', width=2)
    ))
    if r > 0:
        e_actual = k * abs(q) / r**2
        fig.add_trace(go.Scatter(
            x=[r],
            y=[e_actual],
            mode='markers',
            name=f'E({r:.1f}m)',
            marker=dict(color='red', size=10, symbol='star')
        ))
    fig.update_layout(
        title="⚡ Campo Eléctrico vs Distancia",
        xaxis_title="Distancia r (m)",
        yaxis_title="Campo E (N/C)",
        template="plotly_white",
        font=dict(size=12),
        title_font_size=18,
        yaxis_type="log"
    )
    return fig
def graficar_potencial_electrico_interactivo(q, r, r_max=10.0):
    if r_max <= 0:
        r_max = 10.0
    r_vals = np.linspace(0.1, r_max, 200)
    k = 8.99e9
    v_vals = k * q / r_vals
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=r_vals,
        y=v_vals,
        mode='lines',
        name='V(r) teórico',
        line=dict(color='#2ecc71', width=2)
    ))
    if r > 0:
        v_actual = k * q / r
        fig.add_trace(go.Scatter(
            x=[r],
            y=[v_actual],
            mode='markers',
            name=f'V({r:.1f}m)',
            marker=dict(color='red', size=10, symbol='star')
        ))
    fig.update_layout(
        title="🔋 Potencial Eléctrico vs Distancia",
        xaxis_title="Distancia r (m)",
        yaxis_title="Potencial V (V)",
        template="plotly_white",
        font=dict(size=12),
        title_font_size=18
    )
    return fig
def graficar_snell_interactivo(n1, angulo1, n2):
    fig = go.Figure()
    fig.add_shape(type="line", x0=0, y0=-3, x1=0, y1=3, line=dict(color="gray", width=1, dash="dot"))
    fig.add_shape(type="line", x0=-4, y0=0, x1=4, y1=0, line=dict(color="black", width=2))
    theta1_rad = math.radians(angulo1)
    x_inc = -2.5 * math.sin(theta1_rad)
    y_inc = 2.5 * math.cos(theta1_rad)
    fig.add_trace(go.Scatter(x=[x_inc, 0], y=[y_inc, 0], mode='lines', line=dict(color="red", width=4), name="Incidente"))
    sin_theta2 = n1 * math.sin(theta1_rad) / n2
    if abs(sin_theta2) <= 1:
        theta2_rad = math.asin(sin_theta2)
        x_ref = 2.5 * math.sin(theta2_rad)
        y_ref = -2.5 * math.cos(theta2_rad)
        fig.add_trace(go.Scatter(x=[0, x_ref], y=[0, y_ref], mode='lines', line=dict(color="blue", width=4), name="Refractado"))
        fig.add_annotation(x=x_ref/2, y=y_ref/2 - 0.2, text=f"θ₂ = {math.degrees(theta2_rad):.1f}°", showarrow=False, font=dict(color="blue", size=12))
    else:
        x_ref = 2.5 * math.sin(theta1_rad)
        y_ref = 2.5 * math.cos(theta1_rad)
        fig.add_trace(go.Scatter(x=[0, x_ref], y=[0, y_ref], mode='lines', line=dict(color="green", width=4, dash="dot"), name="Reflejado (Total)"))
        fig.add_annotation(x=1.5, y=1.5, text="REFLEXIÓN TOTAL", showarrow=False, font=dict(color="green", size=14, weight="bold"))
    fig.add_annotation(x=-3.5, y=2.5, text=f"Medio 1\nn₁ = {n1}", showarrow=False, font=dict(size=14, color="red"))
    fig.add_annotation(x=-3.5, y=-2.5, text=f"Medio 2\nn₂ = {n2}", showarrow=False, font=dict(size=14, color="blue"))
    fig.add_annotation(x=x_inc/2 - 0.3, y=y_inc/2, text=f"θ₁ = {angulo1}°", showarrow=False, font=dict(color="red", size=12))
    fig.update_layout(
        title="🔍 Ley de Snell: Refracción y Reflexión",
        xaxis=dict(range=[-4, 4], showgrid=False, zeroline=False, showticklabels=False, scaleanchor="y", scaleratio=1),
        yaxis=dict(range=[-3, 3], showgrid=False, zeroline=False, showticklabels=False),
        template="plotly_white",
        showlegend=True,
        width=600,
        height=500,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig
def graficar_onda_senoidal_interactiva(f, lam, longitud_m=3.0):
    if f <= 0 or lam <= 0 or longitud_m <= 0:
        return go.Figure()
    x_vals = np.linspace(0, longitud_m, 500)
    y_vals = np.sin(2 * np.pi * x_vals / lam)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='lines',
        name='Onda',
        line=dict(color='#9b59b6', width=3)
    ))
    fig.update_layout(
        title="🌊 Onda Senoidal",
        xaxis_title="Posición x (m)",
        yaxis_title="Amplitud",
        template="plotly_white",
        font=dict(size=12),
        title_font_size=18
    )
    return fig
def graficar_energia_foton():
    lam_vals = np.linspace(100e-9, 1000e-9, 200)
    h = 6.626e-34
    c = 3e8
    e_vals = h * c / lam_vals
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=lam_vals * 1e9,
        y=e_vals,
        mode='lines',
        name='E(λ)',
        line=dict(color='#f39c12', width=3)
    ))
    fig.update_layout(
        title="🌟 Energía del Fotón vs Longitud de Onda",
        xaxis_title="Longitud de onda λ (nm)",
        yaxis_title="Energía E (J)",
        template="plotly_white",
        font=dict(size=12),
        title_font_size=18
    )
    return fig

# =============== FUNCIONES DE IA ===============
def consultar_ia_fisica_ollama(pregunta: str, modelo: str = "phi3") -> str:
    try:
        prompt = (
            "Eres un profesor de física amable y preciso. "
            "Responde en máximo 3 oraciones, en español, de forma clara y educativa. "
            f"Pregunta del estudiante: '{pregunta}'"
        )
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": modelo,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 150
                }
            },
            timeout=25
        )
        if response.status_code == 200:
            data = response.json()
            return data.get("response", "No pude generar una respuesta.").strip()
        else:
            return "⚠️ La IA local no respondió. ¿Está Ollama activo?"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# =============== INTERFAZ PRINCIPAL ===============
def main():
    st.markdown('<h1 class="main-header">🧠 Aprende Física de Forma Inteligente</h1>', unsafe_allow_html=True)
    # =============== Datos persistentes ===============
    if 'curiosidad_persistente' not in st.session_state:
        st.session_state.curiosidad_persistente = get_random_curiosity()
    # =============== BARRA LATERAL ===============
    with st.sidebar:
        st.markdown("## 📚 Temas Disponibles")
        tema = st.selectbox("Selecciona un módulo",
                           ["🔥 Termodinámica", "⚡ Electricidad y Magnetismo", "🌊 Óptica y Ondas"])
        st.markdown("---")
        st.markdown("### ℹ Instrucciones")
        st.markdown('<div class="sidebar-instructions">Selecciona un tema y subtema. En gráficos interactivos, los resultados se actualizan al cambiar los valores. En otros, utiliza "Calcular".</div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("### 🌟 Dato Curioso")
        text_only = st.session_state.curiosidad_persistente.split(" ", 1)[1] if " " in st.session_state.curiosidad_persistente else st.session_state.curiosidad_persistente
        st.markdown(f'<div class="curiosity-box"><strong>⚡ Hoy aprende esto:</strong><br>{text_only}</div>', unsafe_allow_html=True)
    # Contenido principal
    if tema == "🔥 Termodinámica":
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        show_emoji_header("🔥", "Termodinámica")
        tab_conv, tab_sens, tab_lat, tab_ley1, tab_dil = st.tabs(["Conv. Temp", "Calor Sens", "Calor Lat", "1ra Ley", "Dilatación"])
        with tab_conv:
            col1, col2 = st.columns(2)
            with col1:
                val = st.number_input("Valor", value=0.0, key="conv_val")
            with col2:
                de = st.selectbox("De", ["Celsius", "Kelvin", "Fahrenheit"], key="conv_de")
                a = st.selectbox("A", ["Celsius", "Kelvin", "Fahrenheit"], key="conv_a")
            if st.button("🌡 Convertir", type="primary", key="conv_btn"):
                convertir_temperatura(val, de, a)
        with tab_sens:
            col1, col2, col3 = st.columns(3)
            with col1:
                m = st.number_input("Masa (kg)", value=1.0, key="cs_m")
            with col2:
                c = st.number_input("c (J/kg·K)", value=4186.0, key="cs_c")
            with col3:
                dt = st.number_input("ΔT (°C o K)", value=10.0, key="cs_dt")
            if st.button("🔥 Calcular Calor Sensible", type="primary", key="cs_btn"):
                result = calor_sensible_process(m, c, dt)
                if result is None:
                    show_error_message("La masa y el calor específico deben ser positivos.")
                else:
                    q, steps, unit, desc = result
                    show_calculation_process(
                        formula=r"Q = m \cdot c \cdot \Delta T",
                        steps=steps,
                        result=q,
                        unit=unit,
                        description=desc
                    )
        with tab_lat:
            col1, col2 = st.columns(2)
            with col1:
                m = st.number_input("Masa (kg)", value=1.0, key="cl_m")
            with col2:
                l = st.number_input("L (J/kg)", value=3.34e5, key="cl_l")
            if st.button("❄ Calcular Calor Latente", type="primary", key="cl_btn"):
                result = calor_latente_process(m, l)
                if result is None:
                    show_error_message("La masa y el calor latente deben ser positivos.")
                else:
                    q, steps, unit, desc = result
                    show_calculation_process(
                        formula=r"Q = m \cdot L",
                        steps=steps,
                        result=q,
                        unit=unit,
                        description=desc
                    )
        with tab_ley1:
            col1, col2, col3 = st.columns(3)
            with col1:
                du = st.number_input("ΔU (J)", value=100.0, key="ley1_du")
            with col2:
                q = st.number_input("Q (J) - 0 si no", value=0.0, key="ley1_q")
            with col3:
                w = st.number_input("W (J) - 0 si no", value=0.0, key="ley1_w")
            if st.button("⚡ Calcular Primera Ley", type="primary", key="ley1_btn"):
                if q == 0 and w != 0:
                    result = primera_ley_termodinamica_process(du, w=w)
                elif w == 0 and q != 0:
                    result = primera_ley_termodinamica_process(du, q=q)
                else:
                    show_warning_message("Deja solo un valor en 0.")
                    result = None
                if result is None:
                    show_error_message("Error en los parámetros.")
                else:
                    val, steps, unit, desc = result
                    show_calculation_process(
                        formula=r"\Delta U = Q - W",
                        steps=steps,
                        result=val,
                        unit=unit,
                        description=desc
                    )
        with tab_dil:
            col1, col2 = st.columns(2)
            with col1:
                l0 = st.number_input("Longitud inicial L₀ (m)", value=1.0, format="%.6f", key="dil_l0")
                alpha = st.number_input("Coeficiente α (1/°C)", value=1.2e-5, format="%.2e", key="dil_alpha")
            with col2:
                dt_max = st.number_input("ΔT máximo (°C)", value=100.0, key="dil_dtmax")
            valid = True
            if l0 <= 0:
                st.error("La longitud inicial debe ser positiva.")
                valid = False
            if alpha < 0:
                st.error("El coeficiente de dilatación no puede ser negativo.")
                valid = False
            if dt_max < 0:
                st.error("ΔT máximo no puede ser negativo.")
                valid = False
            if valid:
                dt_ejemplo = dt_max / 2
                l_final = l0 * (1 + alpha * dt_ejemplo)
                show_calculation_process(
                    formula=r"L = L_0(1 + \alpha \Delta T)",
                    steps=[
                        f"L = {l0} * (1 + {alpha} * {dt_ejemplo})",
                        f"L = {l0} * (1 + {alpha * dt_ejemplo})",
                        f"L = {l0} * {1 + alpha * dt_ejemplo}",
                        f"L = {l_final:.6f}"
                    ],
                    result=l_final,
                    unit="m",
                    description="Longitud final después de la dilatación."
                )
                st.plotly_chart(graficar_dilatacion_lineal_interactiva(l0, alpha, dt_max), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    elif tema == "⚡ Electricidad y Magnetismo":
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        show_emoji_header("⚡", "Electricidad y Magnetismo")
        tab_coul, tab_camp, tab_pot, tab_cap, tab_ohm, tab_poten = st.tabs(["Coulomb", "Campo", "Potencial", "Capacitor", "Ohm", "Potencia"])
        with tab_coul:
            col1, col2, col3 = st.columns(3)
            with col1:
                q1 = st.number_input("q₁ (C)", value=1e-6, format="%.2e", key="coul_q1")
            with col2:
                q2 = st.number_input("q₂ (C)", value=1e-6, format="%.2e", key="coul_q2")
            with col3:
                r = st.number_input("r (m)", value=0.1, key="coul_r")
            if st.button("⚡ Calcular Ley de Coulomb", type="primary", key="coul_btn"):
                result = ley_coulomb_process(q1, q2, r)
                if result is None:
                    show_error_message("La distancia debe ser mayor a 0.")
                else:
                    f, steps, unit, desc = result
                    show_calculation_process(
                        formula=r"F = k \frac{|q_1 q_2|}{r^2}",
                        steps=steps,
                        result=f,
                        unit=unit,
                        description=desc
                    )
        with tab_camp:
            col1, col2 = st.columns(2)
            with col1:
                q = st.number_input("Carga q (C)", value=1e-6, format="%.2e", key="camp_q")
            with col2:
                r = st.number_input("Distancia r para resultado (m)", value=1.0, key="camp_r")
                r_max = st.number_input("Distancia máxima para gráfico (m)", value=5.0, min_value=0.1, key="camp_rmax")
            if r <= 0:
                st.error("La distancia debe ser mayor a 0.")
            else:
                result = campo_electrico_process(q, r)
                if result is not None:
                    e_val, steps, unit, desc = result
                    show_calculation_process(
                        formula=r"E = k \frac{|q|}{r^2}",
                        steps=steps,
                        result=e_val,
                        unit=unit,
                        description=desc
                    )
                    st.plotly_chart(graficar_campo_electrico_interactivo(q, r, r_max), use_container_width=True)
        with tab_pot:
            col1, col2 = st.columns(2)
            with col1:
                q = st.number_input("Carga q (C)", value=1e-6, format="%.2e", key="pot_q")
            with col2:
                r = st.number_input("Distancia r para resultado (m)", value=1.0, key="pot_r")
                r_max = st.number_input("Distancia máxima para gráfico (m)", value=5.0, min_value=0.1, key="pot_rmax")
            if r <= 0:
                st.error("La distancia debe ser mayor a 0.")
            else:
                result = potencial_electrico_process(q, r)
                if result is not None:
                    v_val, steps, unit, desc = result
                    show_calculation_process(
                        formula=r"V = k \frac{q}{r}",
                        steps=steps,
                        result=v_val,
                        unit=unit,
                        description=desc
                    )
                    st.plotly_chart(graficar_potencial_electrico_interactivo(q, r, r_max), use_container_width=True)
        with tab_cap:
            col1, col2 = st.columns(2)
            with col1:
                c = st.number_input("C (F)", value=10e-6, format="%.2e", key="cap_c")
            with col2:
                v = st.number_input("V (V)", value=12.0, key="cap_v")
            if st.button("🔋 Calcular Energía en Capacitor", type="primary", key="cap_btn"):
                result = capacitor_energia_process(c, v)
                if result is None:
                    show_error_message("La capacidad y el voltaje deben ser no negativos.")
                else:
                    u, steps, unit, desc = result
                    show_calculation_process(
                        formula=r"U = \frac{1}{2} C V^2",
                        steps=steps,
                        result=u,
                        unit=unit,
                        description=desc
                    )
        with tab_ohm:
            col1, col2, col3 = st.columns(3)
            with col1:
                v = st.number_input("V (V) - 0 si no", value=0.0, key="ohm_v")
            with col2:
                i = st.number_input("I (A) - 0 si no", value=0.0, key="ohm_i")
            with col3:
                r = st.number_input("R (Ω) - 0 si no", value=0.0, key="ohm_r")
            if st.button("⚡ Calcular Ley de Ohm", type="primary", key="ohm_btn"):
                result = ley_ohm_process(
                    v if v != 0 else None,
                    i if i != 0 else None,
                    r if r != 0 else None
                )
                if result is None:
                    show_error_message("Ingrese exactamente dos valores o evite divisiones por cero.")
                else:
                    val, steps, unit, desc = result
                    show_calculation_process(
                        formula=r"V = I \cdot R",
                        steps=steps,
                        result=val,
                        unit=unit,
                        description=desc
                    )
        with tab_poten:
            col1, col2, col3 = st.columns(3)
            with col1:
                v = st.number_input("V (V)", value=0.0, key="poten_v")
            with col2:
                i = st.number_input("I (A)", value=0.0, key="poten_i")
            with col3:
                r = st.number_input("R (Ω)", value=0.0, key="poten_r")
            if st.button("💡 Calcular Potencia Eléctrica", type="primary", key="poten_btn"):
                result = potencia_electrica_process(
                    v if v != 0 else None,
                    i if i != 0 else None,
                    r if r != 0 else None
                )
                if result is None:
                    show_error_message("Ingrese al menos dos valores válidos (V, I, R) y evite divisiones por cero.")
                else:
                    val, steps, unit, desc = result
                    show_calculation_process(
                        formula=r"P = V \cdot I = I^2 \cdot R = \frac{V^2}{R}",
                        steps=steps,
                        result=val,
                        unit=unit,
                        description=desc
                    )
        st.markdown('</div>', unsafe_allow_html=True)
    elif tema == "🌊 Óptica y Ondas":
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        show_emoji_header("🌊", "Óptica y Ondas")
        tab_fp, tab_vo, tab_ef, tab_snell = st.tabs(["Frec/Per", "Vel Onda", "Energía Fotón", "Snell"])
        with tab_fp:
            col1, col2 = st.columns(2)
            with col1:
                f = st.number_input("f (Hz) - 0 si no", value=0.0, key="fp_f")
            with col2:
                t = st.number_input("T (s) - 0 si no", value=0.0, key="fp_t")
            if st.button("🔄 Calcular Frecuencia/Período", type="primary", key="fp_btn"):
                result = frecuencia_periodo_process(
                    f if f != 0 else None,
                    t if t != 0 else None
                )
                if result is None:
                    show_error_message("Ingrese un valor distinto de 0 para calcular el otro.")
                else:
                    val, steps, unit, desc = result
                    show_calculation_process(
                        formula=r"f = \frac{1}{T} \quad \text{o} \quad T = \frac{1}{f}",
                        steps=steps,
                        result=val,
                        unit=unit,
                        description=desc
                    )
        with tab_vo:
            col1, col2 = st.columns(2)
            with col1:
                f = st.number_input("Frecuencia f (Hz)", value=440.0, key="vo_f")
                lam = st.number_input("Longitud de onda λ (m)", value=0.78, key="vo_lam")
            with col2:
                if f > 0 and lam > 0:
                    result = velocidad_onda_process(f, lam)
                    if result is not None:
                        v, steps, unit, desc = result
                        show_calculation_process(
                            formula=r"v = f \cdot \lambda",
                            steps=steps,
                            result=v,
                            unit=unit,
                            description=desc
                        )
                        st.plotly_chart(graficar_onda_senoidal_interactiva(f, lam), use_container_width=True)
                else:
                    if f <= 0:
                        st.error("La frecuencia debe ser positiva.")
                    if lam <= 0:
                        st.error("La longitud de onda debe ser positiva.")
        with tab_ef:
            col1, col2 = st.columns(2)
            with col1:
                f = st.number_input("Frecuencia f (Hz) - 0 si usa λ", value=0.0, key="ef_f")
            with col2:
                lam = st.number_input("Longitud de onda λ (m) - 0 si usa f", value=500e-9, format="%.2e", key="ef_lam")
            if st.button("🌟 Calcular y Graficar", type="primary", key="ef_btn"):
                if f != 0:
                    result = energia_foton_process(f=f)
                elif lam != 0:
                    result = energia_foton_process(lam=lam)
                else:
                    st.error("Ingrese frecuencia o longitud de onda.")
                    result = None
                if result is not None:
                    e, steps, unit, desc = result
                    show_calculation_process(
                        formula=r"E = h \cdot f = \frac{h \cdot c}{\lambda}",
                        steps=steps,
                        result=e,
                        unit=unit,
                        description=desc
                    )
                    st.plotly_chart(graficar_energia_foton(), use_container_width=True)
        with tab_snell:
            st.markdown("<h5 style='color:#2c3e50;'>Simula cómo la luz se dobla al pasar de un material a otro.</h5>", unsafe_allow_html=True)
            materiales = {
                "Vacío": 1.000,
                "Aire": 1.0003,
                "Hielo": 1.31,
                "Agua": 1.333,
                "Etanol": 1.36,
                "Cuarzo": 1.46,
                "Vidrio (crown)": 1.52,
                "Vidrio (flint)": 1.66,
                "Zafiro": 1.77,
                "Diamante": 2.417,
                "Germanio (IR)": 4.05
            }
            col1, col2 = st.columns([2, 3])
            with col1:
                st.markdown("#### 🧪 Parámetros de Entrada")
                # Inicializar estado de sesión si no existe
                if 'n1_selected' not in st.session_state:
                    st.session_state.n1_selected = "Aire"
                    st.session_state.n1_manual = materiales["Aire"]
                    st.session_state.n1_is_manual = False
                if 'n2_selected' not in st.session_state:
                    st.session_state.n2_selected = "Agua"
                    st.session_state.n2_manual = materiales["Agua"]
                    st.session_state.n2_is_manual = False
                # Función para actualizar n1 desde material (siempre, incluso si fue editado)
                def update_n1_from_material():
                    st.session_state.n1_manual = materiales[st.session_state.mat1]
                    st.session_state.n1_selected = st.session_state.mat1
                    st.session_state.n1_is_manual = False  # Resetear a automático
                # Función para bloquear n1 cuando se edita manualmente
                def lock_n1():
                    st.session_state.n1_is_manual = True
                # Función para actualizar n2 desde material (siempre, incluso si fue editado)
                def update_n2_from_material():
                    st.session_state.n2_manual = materiales[st.session_state.mat2]
                    st.session_state.n2_selected = st.session_state.mat2
                    st.session_state.n2_is_manual = False  # Resetear a automático
                # Función para bloquear n2 cuando se edita manualmente
                def lock_n2():
                    st.session_state.n2_is_manual = True
                # --- Medio 1 ---
                st.markdown("*Medio 1* (luz incidente)")
                cols_m1 = st.columns(2)
                with cols_m1[0]:
                    material1 = st.selectbox(
                        "Material",
                        list(materiales.keys()),
                        index=list(materiales.keys()).index(st.session_state.n1_selected),
                        key="mat1",
                        on_change=update_n1_from_material
                    )
                with cols_m1[1]:
                    n1_manual = st.number_input(
                        "n₁",
                        value=float(st.session_state.n1_manual),
                        format="%.3f",
                        key="n1_manual",
                        on_change=lock_n1
                    )
                # Mostrar estado
                if st.session_state.n1_is_manual:
                    st.caption("🔸 Valor personalizado")
                else:
                    st.caption(f"🔹 Usando valor de: {st.session_state.n1_selected}")
                st.divider()
                # --- Medio 2 ---
                st.markdown("*Medio 2* (luz refractada)")
                cols_m2 = st.columns(2)
                with cols_m2[0]:
                    material2 = st.selectbox(
                        "Material",
                        list(materiales.keys()),
                        index=list(materiales.keys()).index(st.session_state.n2_selected),
                        key="mat2",
                        on_change=update_n2_from_material
                    )
                with cols_m2[1]:
                    n2_manual = st.number_input(
                        "n₂",
                        value=float(st.session_state.n2_manual),
                        format="%.3f",
                        key="n2_manual",
                        on_change=lock_n2
                    )
                # Mostrar estado
                if st.session_state.n2_is_manual:
                    st.caption("🔸 Valor personalizado")
                else:
                    st.caption(f"🔹 Usando valor de: {st.session_state.n2_selected}")
                st.divider()
                ang1 = st.slider("Ángulo de incidencia θ₁ (°)", min_value=0, max_value=90, value=30, key="snell_ang1", help="Ángulo entre el rayo incidente y la normal.")
                valid = True
                if n1_manual <= 0 or n2_manual <= 0:
                    st.error("❌ Los índices de refracción deben ser positivos.")
                    valid = False
                if ang1 < 0 or ang1 > 90:
                    st.error("❌ El ángulo debe estar entre 0° y 90°.")
                    valid = False
            with col2:
                st.markdown("#### 🔍 Resultado y Diagrama")
                if valid:
                    result = ley_snell_process(n1_manual, ang1, n2_manual)
                    if result is None:
                        show_warning_message("Reflexión total interna. La luz se refleja completamente en la interfaz.")
                    else:
                        theta2, steps, unit, desc = result
                        show_calculation_process(
                            formula=r"n_1 \sin(\theta_1) = n_2 \sin(\theta_2)",
                            steps=steps,
                            result=theta2,
                            unit=unit,
                            description=desc
                        )
                    st.plotly_chart(graficar_snell_interactivo(n1_manual, ang1, n2_manual), use_container_width=True)
                else:
                    st.info("Ajuste los parámetros para ver la simulación.")
            with st.expander("📖 Índices de refracción de materiales comunes"):
                st.table(materiales)
        st.markdown('</div>', unsafe_allow_html=True)

    # =============== IA LOCAL ===============
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    show_emoji_header("🧠", "Asistente de IA (Física Local)")
    st.markdown("ℹ️ Requiere **Ollama + phi3** instalado en esta PC.")
    pregunta = st.text_input("Escribe tu duda de física (ej: ¿por qué el cielo es azul?)")
    if st.button("🧠 Consultar a la IA") and pregunta.strip():
        with st.spinner("Pensando..."):
            respuesta = consultar_ia_fisica_ollama(pregunta.strip())
        st.markdown(f'<div class="explanation-box">{respuesta}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =============== ¡CORREGIDA! ===============


if __name__ == "__main__":  # <-- CORREGIDO: dos guiones bajos
    main()

