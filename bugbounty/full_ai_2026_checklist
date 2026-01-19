# Comprehensive AI/ML Bug Bounty Reconnaissance & Testing Checklist

## **Phase 1: AI-Specific Reconnaissance**

### **AI Component Discovery**
- Identify AI/ML endpoints (`/api/v1/predict`, `/model/inference`, `/ai/chat`)
- Locate model serving endpoints (TensorFlow Serving, TorchServe, Triton)
- Find model training/management interfaces (`/mlflow`, `/kubeflow`, `/train`)
- Discover AI API documentation (Swagger/OpenAPI for AI services)
- Identify WebSocket endpoints for real-time AI inference
- Find GraphQL endpoints with AI-related queries/mutations
- Locate WebRTC connections for AI-powered video/audio processing

### **AI Service Fingerprinting**
- Identify ML frameworks (TensorFlow, PyTorch, Scikit-learn, ONNX)
- Detect model formats (`.h5`, `.pb`, `.pt`, `.onnx`, `.joblib`)
- Recognize AI hardware accelerators (GPU endpoints, TPU, Inferentia)
- Map AI microservices architecture
- Identify containerized AI services (Docker, Kubernetes AI pods)
- Discover serverless AI functions (AWS Lambda, Google Cloud Functions)
- Find edge AI deployment endpoints

### **AI Data Pipeline Discovery**
- Locate data ingestion endpoints
- Identify feature store APIs
- Find data labeling interfaces
- Discover data versioning systems (DVC endpoints)
- Locate data preprocessing services
- Identify data augmentation endpoints
- Find synthetic data generation services

## **Phase 2: AI Model Interaction Testing**

### **Prompt Injection & Manipulation**
- Test for direct prompt injection in LLM systems
- Attempt indirect prompt injection through data sources
- Test for prompt leakage via error messages
- Attempt model jailbreaking techniques
- Test for training data extraction via prompts
- Attempt privilege escalation through prompt engineering
- Test for context window overflow attacks
- Attempt prompt injection in multi-step AI workflows

### **Model Evasion & Adversarial Attacks**
- Test with adversarial examples (images, text, audio)
- Attempt model inversion attacks
- Test membership inference attacks
- Attempt model stealing/reconstruction
- Test for transferability of adversarial examples
- Attempt data poisoning through API inputs
- Test model fairness/ bias exploitation
- Attempt backdoor trigger activation

### **Model Data Exploitation**
- Test for training data extraction
- Attempt model parameter extraction
- Test for data leakage in predictions
- Attempt sensitive information reconstruction
- Test for model memorization attacks
- Attempt differential privacy bypass
- Test for dataset fingerprinting
- Attempt synthetic data reverse engineering

## **Phase 3: AI API & Endpoint Security**

### **API-Specific AI Testing**
- Test for excessive resource consumption (model inference)
- Attempt API rate limit bypass for AI endpoints
- Test for model version confusion attacks
- Attempt hot-swapping of model versions
- Test for unauthorized model deployment
- Attempt training job injection/modification
- Test for inference pipeline manipulation
- Attempt batch processing job hijacking

### **AI Authentication & Authorization**
- Test for model access without authentication
- Attempt privilege escalation to premium AI models
- Test for API key reuse across AI services
- Attempt JWT token manipulation for AI endpoints
- Test for SSO bypass in AI dashboards
- Attempt OAuth token theft from AI applications
- Test for hardcoded credentials in AI containers
- Attempt service account privilege escalation

## **Phase 4: AI Infrastructure & Deployment**

### **Container & Orchestration Security**
- Test for exposed Docker sockets in AI containers
- Attempt container breakout from ML workloads
- Test for sensitive data in container images
- Attempt Kubernetes API server access
- Test for exposed GPU/driver interfaces
- Attempt node takeover via AI workloads
- Test for insecure volume mounts in AI pods
- Attempt cross-tenant access in multi-tenant AI clusters

### **Model Repository & Registry**
- Test for unauthorized model upload/download
- Attempt model tampering in registry
- Test for model version manipulation
- Attempt poisoning of public model repositories
- Test for insecure model artifact storage
- Attempt metadata injection in model registry
- Test for race conditions in model deployment
- Attempt denial of service on model serving

## **Phase 5: AI Data Pipeline Security**

### **Training Pipeline Exploitation**
- Test for training data poisoning
- Attempt feature manipulation attacks
- Test for label flipping attacks
- Attempt hyperparameter manipulation
- Test for gradient leakage attacks
- Attempt federated learning compromise
- Test for distributed training attacks
- Attempt checkpoint poisoning

### **Feature Store & Data Validation**
- Test for feature injection attacks
- Attempt feature store pollution
- Test for statistical skew attacks
- Attempt data drift exploitation
- Test for schema poisoning
- Attempt data lineage manipulation
- Test for metadata corruption
- Attempt data version rollback attacks

## **Phase 6: AI Client-Side Security**

### **Browser-Based AI Exploits**
- Test WebGL-based ML model exploitation
- Attempt TensorFlow.js model theft
- Test for client-side model poisoning
- Attempt WebAssembly ML module attacks
- Test for model caching attacks
- Attempt local storage model manipulation
- Test for IndexedDB ML data extraction
- Attempt service worker ML model hijacking

### **Mobile AI Application Testing**
- Test for exposed Core ML/TFLite models
- Attempt model extraction from mobile apps
- Test for insecure model storage on device
- Attempt ML kit/ARKit exploitation
- Test for biometric AI model bypass
- Attempt on-device training data leakage
- Test for model update mechanism attacks
- Attempt federated learning client compromise

## **Phase 7: AI Supply Chain Security**

### **Third-Party AI Components**
- Test for vulnerable ML library dependencies
- Attempt poisoned pre-trained model attacks
- Test for malicious AI pipelines/notebooks
- Attempt supply chain attacks via AI datasets
- Test for compromised AI SaaS integrations
- Attempt API key leakage through AI services
- Test for vulnerable Jupyter kernels
- Attempt notebook injection attacks

### **AI Development Tools**
- Test for exploitation in ML development environments
- Attempt code injection in AI notebooks
- Test for credential leakage in AI tool configurations
- Attempt backdoor insertion in AutoML pipelines
- Test for model serialization vulnerabilities
- Attempt pickle exploitation in ML models
- Test for insecure ML experiment tracking
- Attempt MLflow artifact tampering

## **Phase 8: Advanced AI-Specific Attacks**

### **Multimodal AI Exploitation**
- Test cross-modal injection attacks
- Attempt vision-language model manipulation
- Test for audio-visual AI system bypass
- Attempt sensor fusion exploitation
- Test for multimodal data poisoning
- Attempt cross-domain adversarial attacks
- Test for coordinated multi-model attacks
- Attempt ensemble model manipulation

### **Reinforcement Learning Attacks**
- Test for reward hacking
- Attempt environment poisoning
- Test for policy extraction
- Attempt training process manipulation
- Test for exploration exploitation
- Attempt transfer learning attacks
- Test for multi-agent system compromise
- Attempt meta-learning manipulation

## **Phase 9: AI Privacy & Compliance**

### **Privacy Attack Vectors**
- Test for model inversion privacy breaches
- Attempt attribute inference attacks
- Test for property inference attacks
- Attempt reconstruction attacks
- Test for privacy budget exploitation
- Attempt differential privacy parameter attacks
- Test for secure aggregation bypass
- Attempt homomorphic encryption side-channels

### **Regulatory Compliance Testing**
- Test for GDPR violations in AI systems
- Attempt HIPAA data leakage through ML
- Test for CCPA/CPRA AI compliance issues
- Attempt PCI DSS bypass via ML systems
- Test for algorithmic bias/ discrimination
- Attempt fairness metric manipulation
- Test for explainability/AI transparency
- Attempt accountability bypass in AI decisions

## **Phase 10: Specialized AI Systems**

### **Computer Vision Systems**
- Test for adversarial patch attacks
- Attempt physical world attacks on CV systems
- Test for object detection bypass
- Attempt facial recognition spoofing
- Test for image segmentation manipulation
- Attempt OCR system poisoning
- Test for video analysis exploitation
- Attempt depth estimation attacks

### **NLP & Language Models**
- Test for toxic content generation bypass
- Attempt sentiment analysis manipulation
- Test for text classification evasion
- Attempt named entity recognition attacks
- Test for machine translation poisoning
- Attempt text summarization manipulation
- Test for chatbot security bypass
- Attempt code generation exploitation

### **Autonomous & Robotics Systems**
- Test for sensor spoofing attacks
- Attempt control signal manipulation
- Test for planning algorithm exploitation
- Attempt SLAM system attacks
- Test for reinforcement learning policy hacking
- Attempt sim-to-real transfer attacks
- Test for multi-robot system compromise
- Attempt human-in-the-loop manipulation

## **Phase 11: AI Monitoring & Detection Evasion**

### **AI Security Bypass**
- Test for anomaly detection evasion
- Attempt fraud detection system bypass
- Test for intrusion detection ML evasion
- Attempt spam filter poisoning
- Test for malware detection ML bypass
- Attempt CAPTCHA solving through ML
- Test for biometric system spoofing
- Attempt behavior analysis evasion

### **Defensive AI Exploitation**
- Test for adversarial training bypass
- Attempt defensive distillation attacks
- Test for gradient masking exploitation
- Attempt certified defense bypass
- Test for ensemble defense manipulation
- Attempt detection-based defense evasion
- Test for input transformation bypass
- Attempt randomization defense attacks

## **Phase 12: AI Incident Response & Forensics**

### **Attack Detection & Analysis**
- Test for ML attack detection capabilities
- Attempt forensic evidence manipulation
- Test for attack attribution bypass
- Attempt log poisoning in AI systems
- Test for metric manipulation attacks
- Attempt alert fatigue through AI systems
- Test for incident response automation bypass
- Attempt recovery process manipulation

## **Automation & Tooling Recommendations**

### **AI-Specific Tools**
- **Adversarial Testing**: ART, CleverHans, Foolbox, TextAttack
- **Model Analysis**: SHAP, LIME, Captum, TensorBoard
- **ML Security**: Microsoft Counterfit, IBM Adversarial Robustness Toolbox
- **Data Poisoning**: Poison Frogs, Backdoor Attacks Toolkit
- **Model Stealing**: Knockoff Nets, ModelExtraction
- **Membership Inference**: ML Privacy Meter, Shadow Models
- **Prompt Security**: Garak, PromptInject, LM Jailbreak
- **AI Fuzzing**: DeepHunter, TensorFuzz, MLFuzz

### **Custom Automation Scripts**
- Automated prompt injection payload generator
- Adversarial example generation pipeline
- Model extraction automation
- Training data inference scripts
- AI API fuzzing framework
- Model serialization vulnerability scanner
- Containerized AI environment tester
- Federated learning attack simulator

## **Reporting Guidelines for AI Vulnerabilities**

### **Required Documentation**
- Detailed attack methodology
- Impact on model performance metrics
- Data leakage quantification
- Privacy violation evidence
- Reproducible attack code
- Mitigation recommendations
- CVSS scoring for AI systems
- Regulatory impact assessment

### **Priority Classification**
- **Critical**: Training data extraction, model theft, RCE via ML
- **High**: Prompt injection, data poisoning, adversarial evasion
- **Medium**: Model inversion, membership inference
- **Low**: Model bias, fairness issues without security impact


**Note**: This checklist is specifically tailored for AI/ML systems and should be used alongside traditional web application security testing methodologies. Always ensure you have proper authorization before testing any system.

**Source**
https://UndercodeTesting.com
