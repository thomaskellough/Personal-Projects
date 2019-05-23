//
//  ViewController.swift
//  BullsEye
//
//  Created by Thomas Kellough on 5/20/19.
//  Copyright © 2019 Thomas Kellough. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    var currentValue = 0
    var targetValue = 0
    var score = 0
    var round = 1
    
    @IBOutlet weak var slider: UISlider!
    @IBOutlet weak var targetLabel: UILabel!
    @IBOutlet weak var targetLabelScore: UILabel!
    @IBOutlet weak var targetLabelRound: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        let roundedValue = slider.value.rounded()
        currentValue = Int(roundedValue)
        startNewRound()
        startOver()
        
        let thumbImageNormal = #imageLiteral(resourceName: "SliderThumb-Normal")
        slider.setThumbImage(thumbImageNormal, for: .normal)
        
        let thumbImageHighlighted = #imageLiteral(resourceName: "SliderThumb-Highlighted")
        slider.setThumbImage(thumbImageHighlighted, for: .highlighted)
        
        let insets = UIEdgeInsets(top: 0, left: 14, bottom: 0, right: 14)
        
        let trackLeftImage = #imageLiteral(resourceName: "SliderTrackLeft")
        let trackLeftResizable = trackLeftImage.resizableImage(withCapInsets: insets)
        slider.setMinimumTrackImage(trackLeftResizable, for: .normal)
        
        let trackRightImage = #imageLiteral(resourceName: "SliderTrackRight")
        let trackRightResizable = trackRightImage.resizableImage(withCapInsets: insets)
        slider.setMaximumTrackImage(trackRightResizable, for: .normal)
        
    }

    @IBAction func showAlert() {
        
        let difference = abs(currentValue - targetValue)
        var points = 100 - difference
        
        switch difference {
        case 0:
            title = "Perfect!"
            points += 100
        case 1:
            title = "Near miss!"
            points += 50
        case 2...5:
            title = "Close one!"
        default:
            title = "Not even close!"
        }
        
        score += points
        round += 1

        let message = "You scored \(points) points!"
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        let action = UIAlertAction(title: "OK", style: .default, handler: {
            action in
            self.startNewRound()
        })
        alert.addAction(action)
        present(alert, animated: true, completion: nil)
        
    }
    
    @IBAction func sliderMoved(_ slider: UISlider) {
        let roundedValue = slider.value.rounded()
        currentValue = Int(roundedValue)
    }
    
    func startNewRound() {
        targetValue = Int.random(in: 1...100)
        currentValue = 50
        slider.value = Float(currentValue)
        updateLabels()
        updateScore()
        updateRound()
    }
    
    func updateLabels() {
        targetLabel.text = String(targetValue)
    }
    
    func updateScore() {
        targetLabelScore.text = String(score)
    }
    
    func updateRound() {
        targetLabelRound.text = String(round)
    }
    
    @IBAction func startOver() {
        score = 0
        round = 1
        updateScore()
        updateRound()
    }
}

