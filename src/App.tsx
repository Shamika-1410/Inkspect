import React from 'react';
import {
  Brain,
  Shield,
  Upload,
  BarChart3,
  Zap,
  CheckCircle,
  Database,
  FileCheck,
  ArrowRight,
  Lock,
} from 'lucide-react';

import img from './img.png'

function FeatureCard({ icon: Icon, title, description }: {
  icon: React.ElementType;
  title: string;
  description: string;
}) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-lg hover:shadow-xl transition-shadow">
      <div className="h-12 w-12 bg-red-50 rounded-lg flex items-center justify-center mb-4">
        <Icon className="h-6 w-6 text-red-800" />
      </div>
      <h3 className="text-xl font-semibold mb-2">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </div>
  );
}

function StepCard({ number, title, description }: {
  number: number;
  title: string;
  description: string;
}) {
  return (
    <div className="flex items-start space-x-4">
      <div className="flex-shrink-0 h-10 w-10 rounded-full bg-red-800 flex items-center justify-center text-white font-bold">
        {number}
      </div>
      <div>
        <h3 className="text-lg font-semibold mb-1">{title}</h3>
        <p className="text-gray-600">{description}</p>
      </div>
    </div>
  );
}

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Hero Section */}
      <header className="bg-gradient-to-r from-red-900  my-auto to-red-800 py-10 text-white">
        <img src={img} alt="" className='mx-auto -mt-10'/>
        <div className="container mx-auto px-6">
          <div className="max-w-4xl mx-auto text-center">
            <h1 className="text-5xl font-bold mb-6">
              Advanced Signature Forgery Detection  
            </h1>
            <p className="text-xl mb-8">
              Powered by Vision Transformers and Machine Learning to protect your documents
              with state-of-the-art forgery detection
            </p>
            <button className="bg-white text-red-900 px-8 py-3 rounded-lg font-semibold hover:bg-red-50 transition-colors inline-flex items-center">
              Get Started
              <ArrowRight className="ml-2 h-5 w-5" />
            </button>
          </div>
        </div>
      </header>

      {/* Features Section */}
      <section className="py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-3xl font-bold text-center mb-12">
            Comprehensive Signature Analysis
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <FeatureCard
              icon={Brain}
              title="AI-Powered Detection"
              description="Advanced Vision Transformer model trained on extensive signature datasets"
            />
            <FeatureCard
              icon={Shield}
              title="High Accuracy"
              description="99%+ accuracy in detecting forged signatures across various styles"
            />
            <FeatureCard
              icon={BarChart3}
              title="Detailed Analysis"
              description="In-depth analysis of signature characteristics and confidence scores"
            />
            <FeatureCard
              icon={Database}
              title="Robust Dataset"
              description="Trained on diverse signature samples from multiple domains"
            />
            <FeatureCard
              icon={Zap}
              title="Real-time Processing"
              description="Instant verification results for quick decision making"
            />
            <FeatureCard
              icon={Lock}
              title="Secure System"
              description="Enterprise-grade security for sensitive signature data"
            />
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section className="bg-white py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-3xl font-bold text-center mb-12">How It Works</h2>
          <div className="max-w-3xl mx-auto space-y-12">
            <StepCard
              number={1}
              title="Upload Signature"
              description="Upload the signature image you want to verify through our secure interface"
            />
            <StepCard
              number={2}
              title="AI Analysis"
              description="Our Vision Transformer model analyzes multiple aspects of the signature"
            />
            <StepCard
              number={3}
              title="Detailed Results"
              description="Receive comprehensive results with confidence scores and analysis"
            />
            <StepCard
              number={4}
              title="Export Report"
              description="Generate detailed verification reports for documentation"
            />
          </div>
        </div>
      </section>

      {/* Statistics Section */}
      

      {/* CTA Section */}
      <section className="py-20">
        <div className="container mx-auto px-6 text-center">
          <h2 className="text-3xl font-bold mb-8">
            Ready to Enhance Your Signature Verification?
          </h2>
          <button className="bg-red-800 text-white px-8 py-3 rounded-lg font-semibold hover:bg-red-900 transition-colors inline-flex items-center">
            Start Free Trial
            <ArrowRight className="ml-2 h-5 w-5" />
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-300 py-12">
        <div className="container mx-auto px-6">
          <div className="text-center">
            <p>&copy; 2024 Inkspect. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;