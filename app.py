import gradio as gr
from MedAI_Maincode import ChatBot,BrainTumor,Detectskindisease,Pneumonia
js = """
function createGradioAnimation() {
    var container = document.createElement('div');
    container.id = 'gradio-animation';
    container.style.fontSize = '2em';
    container.style.fontWeight = 'bold';
    container.style.textAlign = 'center';
    container.style.marginBottom = '20px';

    var text = 'Welcome to Hera!';
    for (var i = 0; i < text.length; i++) {
        (function(i){
            setTimeout(function(){
                var letter = document.createElement('span');
                letter.style.opacity = '0';
                letter.style.transition = 'opacity 0.5s';
                letter.innerText = text[i];

                container.appendChild(letter);

                setTimeout(function() {
                    letter.style.opacity = '1';
                }, 50);
            }, i * 250);
        })(i);
    }

    var gradioContainer = document.querySelector('.gradio-container');
    gradioContainer.insertBefore(container, gradioContainer.firstChild);

    return 'Animation created';
}
"""
css = """

"""
if __name__ == "__main__":
  Main = gr.TabbedInterface([BrainTumor.create_brain_tumor_detect(), Pneumonia.create_pneumonia_tab(), Detectskindisease.create_skin_tab(),ChatBot.create_chatbot_tab()],
                            tab_names = ["Chẩn Đoán Khối U Não", "Chẩn Đoán Tình Trạng Phổi", "Chẩn Đoán Bệnh Ngoài Da", "Tư Vấn Sức Khỏe Thông Minh"],
                            theme = "HaleyCH/HaleyCH_Theme",
                            js = js)
  Main.launch(share=True,debug=True)
