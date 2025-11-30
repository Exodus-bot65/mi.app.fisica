import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math
import random
import requests  # Necesario para la IA con Ollama

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

# =============== IA LOCAL CON OLLAMA ===============
def consultar_ia_fisica_ollama(pregunta: str, modelo: str = "phi3") -> str:
    """
    Consulta a un modelo de IA local (Ollama) para obtener una explicación breve sobre física.
    Requiere que Ollama esté instalado y corriendo en localhost.
    """
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
    except requests.exceptions.ConnectionError:
        return "❌ No se pudo conectar con Ollama. Asegúrate de que esté instalado y ejecutándose."
    except Exception as e:
        return f"❌ Error inesperado: {str(e)}"

# =============== ESTILOS Y CONFIGURACIÓN ===============
st.set_page_config(
    page_title="Física Inteligente",
    page_icon="🧠",
    layout="wide"
)
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: 700; color: #2c3e50; text-align: center; margin-bottom: 2rem; }
    .module-card { background: white; padding: 1.5rem; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin: 1rem 0; border-left: 4px solid #3498db; }
    .result-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1rem; border-radius: 10px; margin: 1rem 0; }
    .info-box, .explanation-box, .curiosity-box, .sidebar-instructions {
        background: #e3f2fd; padding: 1rem; border-radius: 8px; border-left: 4px solid #2196f3; margin: 1rem 0; font-size: 0.9rem;
    }
    .warning-box { background: #fff3cd; border-left: 4px solid #ffc107; padding: 1rem; border-radius: 0 8px 8px 0; margin: 1rem 0; }
    .error-box { background: #f8d7da; color: #721c24; padding: 1rem; border-radius: 10px; margin: 1rem 0; border: 1px solid #f5c6cb; }
</style>
""", unsafe_allow_html=True)

# =============== FUNCIONES UTILITARIAS ===============
def format_scientific(value, unit):
    if value is None or math.isnan(value) or math.isinf(value):
        return "Indefinido"
    if abs(value) >= 1e5 or (abs(value) < 1e-2 and abs(value) > 0):
        return f"{value:.2e} {unit}"
    else:
        return f"{value:.4g} {unit}"

def show_emoji_header(emoji, text):
    st.markdown(f"### {emoji} {text}")

def show_calculation_process(formula, steps, result, unit, description=""):
    st.latex(formula)
    if steps:
        st.markdown("*Pasos del cálculo:*")
        for step in steps:
            st.code(step, language="python")
    formatted_result = format_scientific(result, unit)
    st.markdown(f"""
    <div class="result-box">
        <h4 style="margin:0; font-size: 1.1rem;">Resultado Final</h4>
        <p style="font-size: 1.3rem; margin: 0.5rem 0;">{formatted_result}</p>
        {f'<p style="margin:0; opacity:0.9;">{description}</p>' if description else ''}
    </div>
    """, unsafe_allow_html=True)

def show_error_message(message):
    st.markdown(f'<div class="error-box">{message}</div>', unsafe_allow_html=True)

def show_warning_message(message):
    st.markdown(f'<div class="warning-box">{message}</div>', unsafe_allow_html=True)

# =============== FUNCIONES DE CÁLCULO ===============
# (Todas tus funciones están incluidas y en orden correcto)
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
    steps = [f"Q = m * c * ΔT", f"Q = {masa} * {c_especifico} * {delta_t}", f"Q = {q:.2f}"]
    return q, steps, "J", "Calor absorbido o liberado por el cambio de temperatura."

def calor_latente_process(masa, l):
    if masa <= 0 or l <= 0:
        return None
    q = masa * l
    steps = [f"Q = m * L", f"Q = {masa} * {l}", f"Q = {q:.2f}"]
    return q, steps, "J", "Calor absorbido o liberado durante un cambio de estado."

def primera_ley_termodinamica_process(delta_u, q=None, w=None):
    try:
        if q is None and w is not None:
            q_calc = delta_u + w
            steps = [f"Q = ΔU + W", f"Q = {delta_u} + {w}", f"Q = {q_calc:.2f}"]
            return q_calc, steps, "J", "Calor transferido al sistema."
        elif w is None and q is not None:
            w_calc = q - delta_u
            steps = [f"W = Q - ΔU", f"W = {q} - {delta_u}", f"W = {w_calc:.2f}"]
            return w_calc, steps, "J", "Trabajo realizado por el sistema."
        else:
            return None
    except:
        return None

def ley_coulomb_process(q1, q2, r, k=8.99e9):
    if r <= 0: return None
    f = k * abs(q1 * q2) / r**2
    steps = [f"F = k * |q₁ * q₂| / r²", f"F = {k:.2e} * |{q1:.2e} * {q2:.2e}| / {r}²", f"F = {f:.2e}"]
    return f, steps, "N", "Fuerza de atracción o repulsión entre las cargas."

def campo_electrico_process(q, r, k=8.99e9):
    if r <= 0: return None
    e = k * abs(q) / r**2
    steps = [f"E = k * |q| / r²", f"E = {k:.2e} * |{q:.2e}| / {r}²", f"E = {e:.2e}"]
    return e, steps, "N/C", "Intensidad del campo eléctrico."

def potencial_electrico_process(q, r, k=8.99e9):
    if r <= 0: return None
    v = k * q / r
    steps = [f"V = k * q / r", f"V = {k:.2e} * {q:.2e} / {r}", f"V = {v:.2e}"]
    return v, steps, "V", "Potencial eléctrico."

def capacitor_energia_process(c, v):
    if c < 0 or v < 0: return None
    u = 0.5 * c * v**2
    steps = [f"U = ½ * C * V²", f"U = 0.5 * {c:.2e} * {v}²", f"U = {u:.2e}"]
    return u, steps, "J", "Energía almacenada en el capacitor."

def ley_ohm_process(v=None, i=None, r=None):
    try:
        if v is None and i is not None and r is not None:
            return i * r, [f"V = I * R", f"V = {i} * {r}", f"V = {i*r:.2f}"], "V", "Diferencia de potencial."
        elif i is None and v is not None and r is not None:
            if r == 0: return None
            return v / r, [f"I = V / R", f"I = {v} / {r}", f"I = {v/r:.2f}"], "A", "Corriente eléctrica."
        elif r is None and v is not None and i is not None:
            if i == 0: return None
            return v / i, [f"R = V / I", f"R = {v} / {i}", f"R = {v/i:.2f}"], "Ω", "Resistencia eléctrica."
        else:
            return None
    except:
        return None

def potencia_electrica_process(v=None, i=None, r=None):
    try:
        if v is not None and i is not None:
            p = v * i
            steps = [f"P = V * I", f"P = {v} * {i}", f"P = {p:.2f}"]
        elif i is not None and r is not None:
            p = i**2 * r
            steps = [f"P = I² * R", f"P = {i}² * {r}", f"P = {p:.2f}"]
        elif v is not None and r is not None:
            if r == 0: return None
            p = v**2 / r
            steps = [f"P = V² / R", f"P = {v}² / {r}", f"P = {p:.2f}"]
        else:
            return None
        return p, steps, "W", "Potencia disipada o generada."
    except:
        return None

def frecuencia_periodo_process(f=None, t=None):
    try:
        if f is None and t is not None and t != 0:
            f_calc = 1 / t
            return f_calc, [f"f = 1 / T", f"f = 1 / {t}", f"f = {f_calc:.2f}"], "Hz", "Frecuencia."
        elif t is None and f is not None and f != 0:
            t_calc = 1 / f
            return t_calc, [f"T = 1 / f", f"T = 1 / {f}", f"T = {t_calc:.4f}"], "s", "Período."
        else:
            return None
    except:
        return None

def velocidad_onda_process(f, lam):
    if f < 0 or lam < 0: return None
    v = f * lam
    steps = [f"v = f * λ", f"v = {f} * {lam}", f"v = {v:.2f}"]
    return v, steps, "m/s", "Velocidad de propagación de la onda."

def energia_foton_process(f=None, lam=None, h=6.626e-34, c=3e8):
    try:
        if f is not None:
            if f < 0: return None
            e = h * f
            steps = [f"E = h * f", f"E = {h:.2e} * {f:.2e}", f"E = {e:.2e}"]
        elif lam is not None:
            if lam <= 0: return None
            e = h * c / lam
            steps = [f"E = h * c / λ", f"E = {h:.2e} * {c:.2e} / {lam:.2e}", f"E = {e:.2e}"]
        else:
            return None
        return e, steps, "J", "Energía de un fotón."
    except:
        return None

def ley_snell_process(n1, angulo1, n2):
    if n1 <= 0 or n2 <= 0: return None
    theta1_rad = math.radians(angulo1)
    sin_theta2 = n1 * math.sin(theta1_rad) / n2
    if abs(sin_theta2) > 1:
        return None, [], "", "Reflexión total interna. La luz se refleja completamente en la interfaz."
    theta2 = math.degrees(math.asin(sin_theta2))
    steps = [f"n₁ * sin(θ₁) = n₂ * sin(θ₂)", f"θ₂ = {theta2:.2f}°"]
    return theta2, steps, "°", "Ángulo de refracción."

# =============== GRÁFICOS ===============
def graficar_dilatacion_lineal_interactiva(l0, alpha, dt_max):
    if l0 <= 0 or alpha < 0 or dt_max < 0: return go.Figure()
    dt_vals = np.linspace(0, dt_max, 100)
    l_vals = l0 * (1 + alpha * dt_vals)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dt_vals, y=l_vals, mode='lines', line=dict(color='#e74c3c', width=3)))
    fig.update_layout(title="🌡 Dilatación Térmica Lineal", xaxis_title="ΔT (°C)", yaxis_title="Longitud L (m)", template="plotly_white")
    return fig

def graficar_campo_electrico_interactivo(q, r, r_max=10.0):
    if r_max <= 0: r_max = 10.0
    r_vals = np.linspace(0.1, r_max, 200)
    k = 8.99e9
    e_vals = k * abs(q) / r_vals**2
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=r_vals, y=e_vals, mode='lines', line=dict(color='#3498db', width=2)))
    if r > 0:
        e_actual = k * abs(q) / r**2
        fig.add_trace(go.Scatter(x=[r], y=[e_actual], mode='markers', marker=dict(color='red', size=10)))
    fig.update_layout(title="⚡ Campo Eléctrico vs Distancia", xaxis_title="r (m)", yaxis_title="E (N/C)", template="plotly_white", yaxis_type="log")
    return fig

def graficar_potencial_electrico_interactivo(q, r, r_max=10.0):
    if r_max <= 0: r_max = 10.0
    r_vals = np.linspace(0.1, r_max, 200)
    k = 8.99e9
    v_vals = k * q / r_vals
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=r_vals, y=v_vals, mode='lines', line=dict(color='#2ecc71', width=2)))
    if r > 0:
        v_actual = k * q / r
        fig.add_trace(go.Scatter(x=[r], y=[v_actual], mode='markers', marker=dict(color='red', size=10)))
    fig.update_layout(title="🔋 Potencial Eléctrico vs Distancia", xaxis_title="r (m)", yaxis_title="V (V)", template="plotly_white")
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
    else:
        fig.add_annotation(x=1.5, y=1.5, text="REFLEXIÓN TOTAL", font=dict(color="green", size=14, weight="bold"))
    fig.update_layout(title="🔍 Ley de Snell", xaxis=dict(range=[-4,4], showticklabels=False), yaxis=dict(range=[-3,3], showticklabels=False), template="plotly_white", width=600, height=500)
    return fig

def graficar_onda_senoidal_interactiva(f, lam, longitud_m=3.0):
    if f <= 0 or lam <= 0 or longitud_m <= 0: return go.Figure()
    x_vals = np.linspace(0, longitud_m, 500)
    y_vals = np.sin(2 * np.pi * x_vals / lam)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', line=dict(color='#9b59b6', width=3)))
    fig.update_layout(title="🌊 Onda Senoidal", xaxis_title="Posición x (m)", yaxis_title="Amplitud", template="plotly_white")
    return fig

def graficar_energia_foton():
    lam_vals = np.linspace(100e-9, 1000e-9, 200)
    h, c = 6.626e-34, 3e8
    e_vals = h * c / lam_vals
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=lam_vals * 1e9, y=e_vals, mode='lines', line=dict(color='#f39c12', width=3)))
    fig.update_layout(title="🌟 Energía del Fotón vs Longitud de Onda", xaxis_title="λ (nm)", yaxis_title="E (J)", template="plotly_white")
    return fig

# =============== INTERFAZ PRINCIPAL ===============
def main():
    st.markdown('<h1 class="main-header">🧠 Aprende Física de Forma Inteligente</h1>', unsafe_allow_html=True)
    
    if 'curiosidad_persistente' not in st.session_state:
        st.session_state.curiosidad_persistente = get_random_curiosity()
    
    with st.sidebar:
        st.markdown("## 📚 Temas Disponibles")
        tema = st.selectbox("Selecciona un módulo", ["🔥 Termodinámica", "⚡ Electricidad y Magnetismo", "🌊 Óptica y Ondas"])
        st.markdown("---")
        st.markdown("### ℹ Instrucciones")
        st.markdown('<div class="sidebar-instructions">Selecciona un tema y subtema. Usa "Calcular" o ajusta valores en gráficos.</div>', unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("### 🌟 Dato Curioso")
        text_only = st.session_state.curiosidad_persistente.split(" ", 1)[1] if " " in st.session_state.curiosidad_persistente else st.session_state.curiosidad_persistente
        st.markdown(f'<div class="curiosity-box"><strong>⚡ Hoy aprende esto:</strong><br>{text_only}</div>', unsafe_allow_html=True)

    # --- Termodinámica ---
    if tema == "🔥 Termodinámica":
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        show_emoji_header("🔥", "Termodinámica")
        tab_conv, tab_sens, tab_lat, tab_ley1, tab_dil = st.tabs(["Conv. Temp", "Calor Sens", "Calor Lat", "1ra Ley", "Dilatación"])
        with tab_conv:
            val = st.number_input("Valor", value=0.0, key="conv_val")
            de = st.selectbox("De", ["Celsius", "Kelvin", "Fahrenheit"], key="conv_de")
            a = st.selectbox("A", ["Celsius", "Kelvin", "Fahrenheit"], key="conv_a")
            if st.button("🌡 Convertir", type="primary", key="conv_btn"):
                convertir_temperatura(val, de, a)
        with tab_sens:
            m = st.number_input("Masa (kg)", value=1.0, key="cs_m")
            c = st.number_input("c (J/kg·K)", value=4186.0, key="cs_c")
            dt = st.number_input("ΔT (°C o K)", value=10.0, key="cs_dt")
            if st.button("🔥 Calcular Calor Sensible", type="primary", key="cs_btn"):
                result = calor_sensible_process(m, c, dt)
                if result: show_calculation_process(r"Q = m \cdot c \cdot \Delta T", *result)
                else: show_error_message("La masa y el calor específico deben ser positivos.")
        with tab_lat:
            m = st.number_input("Masa (kg)", value=1.0, key="cl_m")
            l = st.number_input("L (J/kg)", value=3.34e5, key="cl_l")
            if st.button("❄ Calcular Calor Latente", type="primary", key="cl_btn"):
                result = calor_latente_process(m, l)
                if result: show_calculation_process(r"Q = m \cdot L", *result)
                else: show_error_message("La masa y el calor latente deben ser positivos.")
        with tab_ley1:
            du = st.number_input("ΔU (J)", value=100.0, key="ley1_du")
            q = st.number_input("Q (J) - 0 si no", value=0.0, key="ley1_q")
            w = st.number_input("W (J) - 0 si no", value=0.0, key="ley1_w")
            if st.button("⚡ Calcular Primera Ley", type="primary", key="ley1_btn"):
                if q == 0 and w != 0:
                    result = primera_ley_termodinamica_process(du, w=w)
                elif w == 0 and q != 0:
                    result = primera_ley_termodinamica_process(du, q=q)
                else:
                    show_warning_message("Deja solo un valor en 0.")
                    result = None
                if result: show_calculation_process(r"\Delta U = Q - W", *result)
                else: show_error_message("Error en los parámetros.")
        with tab_dil:
            l0 = st.number_input("Longitud inicial L₀ (m)", value=1.0, format="%.6f", key="dil_l0")
            alpha = st.number_input("Coeficiente α (1/°C)", value=1.2e-5, format="%.2e", key="dil_alpha")
            dt_max = st.number_input("ΔT máximo (°C)", value=100.0, key="dil_dtmax")
            if l0 > 0 and alpha >= 0 and dt_max >= 0:
                dt_ejemplo = dt_max / 2
                l_final = l0 * (1 + alpha * dt_ejemplo)
                show_calculation_process(r"L = L_0(1 + \alpha \Delta T)", [
                    f"L = {l0} * (1 + {alpha} * {dt_ejemplo})",
                    f"L = {l_final:.6f}"
                ], l_final, "m", "Longitud final.")
                st.plotly_chart(graficar_dilatacion_lineal_interactiva(l0, alpha, dt_max), use_container_width=True)
            else:
                st.error("Valores inválidos.")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Electricidad ---
    elif tema == "⚡ Electricidad y Magnetismo":
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        show_emoji_header("⚡", "Electricidad y Magnetismo")
        tabs = st.tabs(["Coulomb", "Campo", "Potencial", "Capacitor", "Ohm", "Potencia"])
        with tabs[0]:  # Coulomb
            q1 = st.number_input("q₁ (C)", value=1e-6, format="%.2e", key="coul_q1")
            q2 = st.number_input("q₂ (C)", value=1e-6, format="%.2e", key="coul_q2")
            r = st.number_input("r (m)", value=0.1, key="coul_r")
            if st.button("⚡ Calcular Ley de Coulomb", type="primary", key="coul_btn"):
                result = ley_coulomb_process(q1, q2, r)
                if result: show_calculation_process(r"F = k \frac{|q_1 q_2|}{r^2}", *result)
                else: show_error_message("La distancia debe ser mayor a 0.")
        with tabs[1]:  # Campo
            q = st.number_input("Carga q (C)", value=1e-6, format="%.2e", key="camp_q")
            r = st.number_input("Distancia r para resultado (m)", value=1.0, key="camp_r")
            r_max = st.number_input("Distancia máxima para gráfico (m)", value=5.0, min_value=0.1, key="camp_rmax")
            if r > 0:
                result = campo_electrico_process(q, r)
                if result: 
                    show_calculation_process(r"E = k \frac{|q|}{r^2}", *result)
                    st.plotly_chart(graficar_campo_electrico_interactivo(q, r, r_max), use_container_width=True)
            else:
                st.error("La distancia debe ser mayor a 0.")
        with tabs[2]:  # Potencial
            q = st.number_input("Carga q (C)", value=1e-6, format="%.2e", key="pot_q")
            r = st.number_input("Distancia r (m)", value=1.0, key="pot_r")
            r_max = st.number_input("Distancia máxima para gráfico (m)", value=5.0, min_value=0.1, key="pot_rmax")
            if r > 0:
                result = potencial_electrico_process(q, r)
                if result:
                    show_calculation_process(r"V = k \frac{q}{r}", *result)
                    st.plotly_chart(graficar_potencial_electrico_interactivo(q, r, r_max), use_container_width=True)
            else:
                st.error("La distancia debe ser mayor a 0.")
        with tabs[3]:  # Capacitor
            c = st.number_input("C (F)", value=10e-6, format="%.2e", key="cap_c")
            v = st.number_input("V (V)", value=12.0, key="cap_v")
            if st.button("🔋 Calcular Energía en Capacitor", type="primary", key="cap_btn"):
                result = capacitor_energia_process(c, v)
                if result: show_calculation_process(r"U = \frac{1}{2} C V^2", *result)
                else: show_error_message("La capacidad y el voltaje deben ser no negativos.")
        with tabs[4]:  # Ohm
            v = st.number_input("V (V) - 0 si no", value=0.0, key="ohm_v")
            i = st.number_input("I (A) - 0 si no", value=0.0, key="ohm_i")
            r = st.number_input("R (Ω) - 0 si no", value=0.0, key="ohm_r")
            if st.button("⚡ Calcular Ley de Ohm", type="primary", key="ohm_btn"):
                result = ley_ohm_process(v if v != 0 else None, i if i != 0 else None, r if r != 0 else None)
                if result: show_calculation_process(r"V = I \cdot R", *result)
                else: show_error_message("Ingrese exactamente dos valores o evite divisiones por cero.")
        with tabs[5]:  # Potencia
            v = st.number_input("V (V)", value=0.0, key="poten_v")
            i = st.number_input("I (A)", value=0.0, key="poten_i")
            r = st.number_input("R (Ω)", value=0.0, key="poten_r")
            if st.button("💡 Calcular Potencia Eléctrica", type="primary", key="poten_btn"):
                result = potencia_electrica_process(v if v != 0 else None, i if i != 0 else None, r if r != 0 else None)
                if result: show_calculation_process(r"P = V \cdot I = I^2 \cdot R = \frac{V^2}{R}", *result)
                else: show_error_message("Ingrese al menos dos valores válidos.")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Óptica y Ondas ---
    elif tema == "🌊 Óptica y Ondas":
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        show_emoji_header("🌊", "Óptica y Ondas")
        tabs = st.tabs(["Frec/Per", "Vel Onda", "Energía Fotón", "Snell"])
        with tabs[0]:  # Frecuencia/Período
            f = st.number_input("f (Hz) - 0 si no", value=0.0, key="fp_f")
            t = st.number_input("T (s) - 0 si no", value=0.0, key="fp_t")
            if st.button("🔄 Calcular Frecuencia/Período", type="primary", key="fp_btn"):
                result = frecuencia_periodo_process(f if f != 0 else None, t if t != 0 else None)
                if result: show_calculation_process(r"f = \frac{1}{T} \quad \text{o} \quad T = \frac{1}{f}", *result)
                else: show_error_message("Ingrese un valor distinto de 0 para calcular el otro.")
        with tabs[1]:  # Velocidad de Onda
            f = st.number_input("Frecuencia f (Hz)", value=440.0, key="vo_f")
            lam = st.number_input("Longitud de onda λ (m)", value=0.78, key="vo_lam")
            if f > 0 and lam > 0:
                result = velocidad_onda_process(f, lam)
                if result:
                    show_calculation_process(r"v = f \cdot \lambda", *result)
                    st.plotly_chart(graficar_onda_senoidal_interactiva(f, lam), use_container_width=True)
            else:
                st.error("Ambos valores deben ser positivos.")
        with tabs[2]:  # Energía del Fotón
            f = st.number_input("Frecuencia f (Hz) - 0 si usa λ", value=0.0, key="ef_f")
            lam = st.number_input("Longitud de onda λ (m) - 0 si usa f", value=500e-9, format="%.2e", key="ef_lam")
            if st.button("🌟 Calcular y Graficar", type="primary", key="ef_btn"):
                if f != 0:
                    result = energia_foton_process(f=f)
                elif lam != 0:
                    result = energia_foton_process(lam=lam)
                else:
                    st.error("Ingrese frecuencia o longitud de onda.")
                    result = None
                if result:
                    show_calculation_process(r"E = h \cdot f = \frac{h \cdot c}{\lambda}", *result)
                    st.plotly_chart(graficar_energia_foton(), use_container_width=True)
        with tabs[3]:  # Snell
            st.markdown("Simula cómo la luz se dobla al pasar de un material a otro.")
            materiales = {
                "Vacío": 1.000, "Aire": 1.0003, "Hielo": 1.31, "Agua": 1.333, "Etanol": 1.36,
                "Cuarzo": 1.46, "Vidrio (crown)": 1.52, "Vidrio (flint)": 1.66,
                "Zafiro": 1.77, "Diamante": 2.417, "Germanio (IR)": 4.05
            }
            col1, col2 = st.columns([2, 3])
            with col1:
                mat1 = st.selectbox("Material 1", list(materiales.keys()), index=1)
                n1 = st.number_input("n₁", value=materiales[mat1], format="%.3f")
                mat2 = st.selectbox("Material 2", list(materiales.keys()), index=3)
                n2 = st.number_input("n₂", value=materiales[mat2], format="%.3f")
                ang1 = st.slider("Ángulo de incidencia θ₁ (°)", 0, 90, 30)
                valid = n1 > 0 and n2 > 0
            with col2:
                if valid:
                    result = ley_snell_process(n1, ang1, n2)
                    if result and result[0] is not None:
                        show_calculation_process(r"n_1 \sin(\theta_1) = n_2 \sin(\theta_2)", *result)
                    else:
                        show_warning_message("Reflexión total interna. La luz se refleja completamente.")
                    st.plotly_chart(graficar_snell_interactivo(n1, ang1, n2), use_container_width=True)
                else:
                    st.error("Los índices deben ser positivos.")
            with st.expander("📖 Índices de refracción"):
                st.table(materiales)
        st.markdown('</div>', unsafe_allow_html=True)

    # =============== IA LOCAL ===============
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    show_emoji_header("🧠", "Asistente de IA (Física Local)")
    st.markdown("ℹ️ Usa **IA real local**. Requiere **Ollama + phi3** instalados en esta PC.")
    pregunta = st.text_input("Escribe tu duda de física (ej: ¿por qué el cielo es azul?)")
    if st.button("🧠 Consultar a la IA") and pregunta.strip():
        with st.spinner("Pensando... (IA local)"):
            respuesta = consultar_ia_fisica_ollama(pregunta.strip())
        st.markdown(f'<div class="explanation-box">{respuesta}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =============== PUNTO DE ENTRADA CORRECTO ===============


if __name__ == "__main__":
    main()

