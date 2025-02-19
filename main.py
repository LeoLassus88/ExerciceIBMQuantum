import os
from qiskit import QuantumCircuit
from qiskit_ibm_provider import IBMProvider
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("IBMQ_API_TOKEN")

if not API_KEY:
    raise ValueError("⚠️ Clé API IBM Quantum manquante")

provider = IBMProvider(token=API_KEY)

backend = provider.get_backend("ibmq_qasm_simulator")

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

job = backend.run(qc)
print(f">>> Job ID: {job.job_id()}")
