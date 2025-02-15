document.addEventListener('DOMContentLoaded', () => {
    const chatbot = {
        isOpen: false,
        init() {
            this.icon = document.querySelector('.chatbot-icon');
            this.window = document.querySelector('.chatbot-window');
            this.closeBtn = document.querySelector('.chatbot-close');
            this.input = document.querySelector('.chatbot-input input');
            this.sendBtn = document.querySelector('.chatbot-input button');
            this.messagesContainer = document.querySelector('.chatbot-messages');
            this.typingIndicator = document.querySelector('.typing-indicator');

            this.bindEvents();
            this.addMessage('Hello! I'm your EcoWaste Assistant. How can I help you today?', 'bot');
        },
        bindEvents() {
            this.icon.addEventListener('click', () => this.toggleWindow());
            this.closeBtn.addEventListener('click', () => this.toggleWindow());
            this.sendBtn.addEventListener('click', () => this.sendMessage());
            this.input.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') this.sendMessage();
            });
        },
        toggleWindow() {
            this.isOpen = !this.isOpen;
            this.window.style.display = this.isOpen ? 'flex' : 'none';
            if (this.isOpen) this.input.focus();
        },
        addMessage(text, sender) {
            const message = document.createElement('div');
            message.className = `message ${sender}`;
            message.innerHTML = `<div class="message-content">${text}</div>`;
            this.messagesContainer.appendChild(message);
            this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
        },
        async processUserMessage(text) {
            const responses = {
                'hello': 'Hi there! How can I assist you with e-waste recycling today?',
                'hi': 'Hello! How can I help you with your e-waste?',
                'help': 'I can help you with: \n- E-waste recycling process\n- Reward points\n- Collection scheduling\n- Product evaluation\nWhat would you like to know more about?',
                'recycle': 'To recycle your e-waste, you can:\n1. List your items manually\n2. Use our smart scanning feature\n3. Schedule a pickup\nWhich method would you prefer?',
                'points': 'You earn points based on the type and condition of your e-waste. These points can be redeemed for rewards or cash. Would you like to know your current points balance?',
                'pickup': 'We offer free pickup services for your e-waste. Would you like to schedule a pickup now?',
                'schedule': 'You can schedule a pickup through your dashboard. Would you like me to guide you through the process?',
                'value': 'The value of your e-waste depends on its type, age, and condition. You can get an instant estimate using our scanning feature. Would you like to try it?'
            };

            this.typingIndicator.style.display = 'block';
            await new Promise(resolve => setTimeout(resolve, 1000));

            let response = 'I'm not sure about that. Could you please rephrase your question or ask about e-waste recycling, points, or pickup services?';
            const lowercaseText = text.toLowerCase();
            
            for (const [keyword, reply] of Object.entries(responses)) {
                if (lowercaseText.includes(keyword)) {
                    response = reply;
                    break;
                }
            }

            this.typingIndicator.style.display = 'none';
            this.addMessage(response, 'bot');
        },
        sendMessage() {
            const text = this.input.value.trim();
            if (text) {
                this.addMessage(text, 'user');
                this.input.value = '';
                this.processUserMessage(text);
            }
        }
    };

    chatbot.init();

    // Function to trigger shake animation
    function shakeIcon() {
        const chatbotIcon = document.querySelector('.chatbot-icon');
        chatbotIcon.classList.add('animate');
        
        // Remove the animate class after animation completes
        setTimeout(() => {
            chatbotIcon.classList.remove('animate');
        }, 4000); // 4 seconds = 3 iterations of 1-second animation + delay
    }

    // Shake icon periodically if chat window is not open
    function startPeriodicShake() {
        if (!document.querySelector('.chatbot-window').classList.contains('active')) {
            shakeIcon();
        }
    }

    // Initial delay before starting periodic shake
    setTimeout(() => {
        // Shake every 30 seconds if window is not open
        setInterval(startPeriodicShake, 30000);
    }, 3000);

    // Shake icon when page loads
    shakeIcon();
});
