import "./style/MainContents.css"



type MainContentsProps = {
    title: string;
    children: React.ReactNode
}

function MainContents ({ title, children }:MainContentsProps) {
    return (
    <div className="container">
        <p className="title">{title}</p>
        <div className="content">
            {children}
        </div>
    </div>
    );
}

export default MainContents